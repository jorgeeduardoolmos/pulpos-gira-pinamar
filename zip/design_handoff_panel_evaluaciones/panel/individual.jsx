/* ============================================================
   individual.jsx — Vista Evaluación Individual
   ============================================================ */

function useIndStats(trimestre, evaluador){
  return useMemo(()=>{
    const I = window.RUGBY.individual;
    const cfg = SCALE_IND;
    const metrics = I.metricas;
    let rows = I.filas.filter(r=>r.t===trimestre);
    if(evaluador && evaluador!=='__all') rows = rows.filter(r=>r.ev===evaluador);

    const players = I.jugadores.map(jug=>{
      const prs = rows.filter(r=>r.jug===jug);
      const metricAvgs={}; let rojos=0, total=0;
      metrics.forEach(m=>{
        const vals = prs.map(r=>r.v[m]).filter(Boolean).map(x=>I.map[x]);
        metricAvgs[m] = vals.length?mean(vals):null;
        prs.forEach(r=>{ if(r.v[m]==='Rojo') rojos++; if(r.v[m]) total++; });
      });
      const present = metrics.map(m=>metricAvgs[m]).filter(v=>v!=null);
      return { jug, metricAvgs, avg:present.length?mean(present):null, rojos, total, n:prs.length };
    }).filter(p=>p.avg!=null);

    const metricStats = metrics.map(m=>{
      const vals=[]; const cnt={Rojo:0,Amarillo:0,Verde:0};
      rows.forEach(r=>{ if(r.v[m]){ vals.push(I.map[r.v[m]]); cnt[r.v[m]]++; } });
      return { m, avg:mean(vals), counts:[cnt.Rojo,cnt.Amarillo,cnt.Verde], n:vals.length };
    });
    const overall = mean(players.map(p=>p.avg));
    const byMetric=[...metricStats].sort((a,b)=>b.avg-a.avg);
    const byAvg=[...players].sort((a,b)=>a.avg-b.avg);
    return { cfg, metrics, players, metricStats, overall,
             mejorMetric:byMetric[0], peorMetric:byMetric[byMetric.length-1],
             foco:byAvg.slice(0,5), referentes:[...byAvg].reverse().slice(0,5),
             evaluadores:I.evaluadores };
  },[trimestre, evaluador]);
}

const shortName = full => {
  const [ap, no] = full.split(',').map(s=>s.trim());
  return no ? `${no} ${ap.split(' ')[0]}` : ap;
};

function IndividualView({trimestre}){
  const [evaluador, setEvaluador] = useState('__all');
  const st = useIndStats(trimestre, evaluador);
  const [sort, setSort] = useState({key:'avg', dir:1}); // worst first
  const [q, setQ] = useState('');
  const [hover, setHover] = useState({r:-1,c:-1});

  const sorted = useMemo(()=>{
    let arr=[...st.players];
    if(q.trim()){ const t=q.toLowerCase(); arr=arr.filter(p=>p.jug.toLowerCase().includes(t)); }
    arr.sort((a,b)=>{
      if(sort.key==='jug') return a.jug.localeCompare(b.jug)*sort.dir;
      if(sort.key==='avg') return ((a.avg)-(b.avg))*sort.dir;
      if(sort.key==='rojos') return (a.rojos-b.rojos)*sort.dir;
      return ((a.metricAvgs[sort.key]??0)-(b.metricAvgs[sort.key]??0))*sort.dir;
    });
    return arr;
  },[st, sort, q]);

  return (
    <div className="stack fade-in">

      {/* control: evaluador */}
      <section>
        <SectionHead title="Promedio de la división" hint={`${st.players.length} jugadores · escala Rojo·Amarillo·Verde (1–3)`}
          right={
            <div style={{display:'flex',alignItems:'center',gap:10}}>
              <span className="zbadge" style={{background:'var(--panel-3)',color:'var(--text-2)'}}>
                Global <b style={{color:zoneOf(st.overall,st.cfg).color,marginLeft:5}}>{r1(st.overall)}</b></span>
              <select className="ctl" value={evaluador} onChange={e=>setEvaluador(e.target.value)}>
                <option value="__all">Todos los evaluadores</option>
                {st.evaluadores.map(ev=>(<option key={ev} value={ev}>Mirada · {ev}</option>))}
              </select>
            </div>}/>
        <div className="grid" style={{gridTemplateColumns:'repeat(5,1fr)'}}>
          {st.metricStats.map(ms=>(
            <div key={ms.m} className="kpi">
              <span className="kpi-accent" style={{background:zoneOf(ms.avg,st.cfg).color}}/>
              <div className="kpi-lbl">{ms.m}</div>
              <div className="kpi-row">
                <span className="kpi-val" style={{color:zoneOf(ms.avg,st.cfg).color}}>{r1(ms.avg)}</span>
                <span className="kpi-max">/ 3</span>
              </div>
              <div style={{marginTop:11}}><DistBar counts={ms.counts}/></div>
              <div style={{display:'flex',justifyContent:'space-between',marginTop:7,fontSize:11,color:'var(--text-4)'}}>
                <span style={{color:'var(--rojo)'}}>{ms.counts[0]}</span>
                <span style={{color:'var(--ambar)'}}>{ms.counts[1]}</span>
                <span style={{color:'var(--verde)'}}>{ms.counts[2]}</span>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Insights */}
      <section>
        <SectionHead title="Lectura rápida" hint="dónde enfocar el trabajo"/>
        <div className="grid" style={{gridTemplateColumns:'repeat(3,1fr)'}}>
          <div className="insight">
            <div className="ins-head" style={{color:'var(--rojo)'}}><Ico d={ICONS.target} size={16}/>Jugadores en foco</div>
            {st.foco.map((p,i)=>(
              <InsightItem key={p.jug} rank={i+1} name={shortName(p.jug)}
                sub={p.rojos>0?`${p.rojos} voto${p.rojos>1?'s':''} en rojo`:'a acompañar'} value={p.avg} cfg={st.cfg}/>
            ))}
          </div>
          <div className="insight">
            <div className="ins-head" style={{color:'var(--verde)'}}><Ico d={ICONS.up} size={16}/>Referentes</div>
            {st.referentes.map((p,i)=>(
              <InsightItem key={p.jug} rank={i+1} name={shortName(p.jug)} sub="se destaca" value={p.avg} cfg={st.cfg}/>
            ))}
          </div>
          <div className="insight">
            <div className="ins-head"><Ico d={ICONS.bolt} size={16}/>Fortaleza y déficit del equipo</div>
            <div style={{fontSize:11.5,color:'var(--text-4)',letterSpacing:'.06em',textTransform:'uppercase',fontWeight:600,marginBottom:2}}>Mejor dimensión</div>
            <InsightItem name={st.mejorMetric.m} sub={`${st.mejorMetric.counts[2]} de ${st.mejorMetric.n} en verde`} value={st.mejorMetric.avg} cfg={st.cfg}/>
            <div style={{fontSize:11.5,color:'var(--text-4)',letterSpacing:'.06em',textTransform:'uppercase',fontWeight:600,margin:'12px 0 2px'}}>Mayor déficit</div>
            <InsightItem name={st.peorMetric.m} sub={`${st.peorMetric.counts[0]} de ${st.peorMetric.n} en rojo`} value={st.peorMetric.avg} cfg={st.cfg}/>
            <div style={{marginTop:14,paddingTop:12,borderTop:'1px solid var(--line)',fontSize:12.5,color:'var(--text-3)',lineHeight:1.5}}>
              {st.foco.filter(p=>p.avg<st.cfg.cuts[0]).length} jugador(es) en zona de riesgo · {st.referentes.filter(p=>p.avg>=st.cfg.cuts[2]).length} destacado(s)
            </div>
          </div>
        </div>
      </section>

      {/* Heatmap */}
      <section>
        <SectionHead title="Mapa de calor por jugador"
          hint="ordenado de menor a mayor promedio — tocá una columna para reordenar"
          right={
            <div style={{position:'relative'}}>
              <span style={{position:'absolute',left:11,top:'50%',transform:'translateY(-50%)',color:'var(--text-4)',display:'flex'}}>
                <Ico d={ICONS.search} size={15}/></span>
              <input className="ctl" style={{paddingLeft:34,width:200}} placeholder="Buscar jugador…"
                value={q} onChange={e=>setQ(e.target.value)}/>
            </div>}/>
        <div className="card card-pad">
          <div className="hm-wrap" onMouseLeave={()=>setHover({r:-1,c:-1})}>
            <table className="heat">
              <thead><tr>
                <th className="rowh" style={{cursor:'pointer'}} onClick={()=>setSort(s=>({key:'jug',dir:s.key==='jug'?-s.dir:1}))}>Jugador</th>
                {st.metrics.map((m,ci)=>(
                  <th key={m} className="col" onClick={()=>setSort(s=>({key:m,dir:s.key===m?-s.dir:-1}))}
                      style={{color:hover.c===ci?'var(--text)':undefined}}>
                    {m}{sort.key===m && <span style={{color:'var(--accent)'}}> {sort.dir>0?'▲':'▼'}</span>}
                  </th>
                ))}
                <th className="col" onClick={()=>setSort(s=>({key:'avg',dir:s.key==='avg'?-s.dir:1}))}
                    style={{color:'var(--text)'}}>Prom.{sort.key==='avg' && <span style={{color:'var(--accent)'}}> {sort.dir>0?'▲':'▼'}</span>}</th>
              </tr></thead>
              <tbody>
                {sorted.map((p,ri)=>(
                  <tr key={p.jug} className={hover.r===ri?'hl':''}>
                    <th className="rowh" style={{color:hover.r===ri?'var(--text)':undefined}}>{shortName(p.jug)}</th>
                    {st.metrics.map((m,ci)=>{
                      const v=p.metricAvgs[m];
                      return (
                        <td key={m} className={'cell'+(hover.r===ri&&hover.c===ci?' hl':'')}
                            onMouseEnter={()=>setHover({r:ri,c:ci})}
                            style={{background:v==null?'var(--panel-3)':scoreColor(v,st.cfg), color:v==null?'var(--text-4)':'#06120c'}}>
                          {v==null?'–':r1(v)}
                        </td>
                      );
                    })}
                    <td className="cell avg" onMouseEnter={()=>setHover({r:ri,c:-1})}>{r1(p.avg)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

      {/* Tabla por jugador */}
      <section>
        <SectionHead title="Detalle por jugador" hint="promedio por dimensión, votos en rojo y distribución"/>
        <div className="card" style={{overflow:'hidden'}}>
          <div style={{overflowX:'auto'}}>
            <table className="dt">
              <thead><tr>
                <Th k="jug" sort={sort} setSort={setSort}>Jugador</Th>
                {st.metrics.map(m=>(<Th key={m} k={m} sort={sort} setSort={setSort} num>{m}</Th>))}
                <Th k="rojos" sort={sort} setSort={setSort} num>Rojos</Th>
                <Th k="avg" sort={sort} setSort={setSort} num>Promedio</Th>
              </tr></thead>
              <tbody>
                {sorted.map(p=>(
                  <tr key={p.jug}>
                    <td className="pname">{p.jug}</td>
                    {st.metrics.map(m=>{
                      const v=p.metricAvgs[m];
                      return <td key={m} className="num">
                        {v==null?<span className="muted">–</span>:
                         <span className="cellpill" style={{background:zoneOf(v,st.cfg).soft,color:zoneOf(v,st.cfg).color}}>{r1(v)}</span>}
                      </td>;
                    })}
                    <td className="num" style={{color:p.rojos>0?'var(--rojo)':'var(--text-4)',fontWeight:600}}>{p.rojos||'—'}</td>
                    <td className="num"><span className="cellpill" style={{background:zoneOf(p.avg,st.cfg).color,color:'#06120c'}}>{r1(p.avg)}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

    </div>
  );
}

Object.assign(window, { IndividualView });
