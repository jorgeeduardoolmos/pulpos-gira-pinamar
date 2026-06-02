/* ============================================================
   staff.jsx — Vista Encuesta Staff
   ============================================================ */

function useStaffStats(trimestre){
  return useMemo(()=>{
    const S = window.RUGBY.staff;
    const rows = S.filas.filter(r=>r.t===trimestre);
    const cfg = SCALE_STAFF;
    const qstats = S.preguntas.map(q=>{
      const scores = rows.map(r=>r.ratings[q]).filter(v=>v!=null);
      return { q, cat:S.qcat[q], avg:mean(scores), sd:stdev(scores), n:scores.length, scores };
    });
    const catStats = Object.keys(S.categorias).map(cat=>{
      const all=[]; S.categorias[cat].forEach(q=>{
        rows.forEach(r=>{ if(r.ratings[q]!=null) all.push(r.ratings[q]); });
      });
      return { cat, avg:mean(all), n:all.length };
    });
    const overall = mean(qstats.map(s=>s.avg));
    const byAvg=[...qstats].sort((a,b)=>b.avg-a.avg);
    const fort=byAvg.slice(0,4);
    const debi=[...byAvg].reverse().slice(0,4);
    const acuerdo=[...qstats].sort((a,b)=>a.sd-b.sd);
    return { rows, cfg, qstats, catStats, overall, fort, debi,
             acuerdoMax:acuerdo.slice(0,3), desacuerdoMax:[...acuerdo].reverse().slice(0,3),
             evaluadores:S.evaluadores };
  },[trimestre]);
}

const CAT_DESC = {
  'Técnica':'Pase, tackle, contacto',
  'Táctica':'Ataque, defensa, decisiones',
  'Emocional':'Actitud, resiliencia, conexión',
  'Staff':'Roles, coordinación, comunicación',
};

function StaffView({trimestre}){
  const st = useStaffStats(trimestre);
  const [catFilter, setCatFilter] = useState(null);
  const [sort, setSort] = useState({key:'avg', dir:-1});

  const visibleQ = st.qstats
    .filter(s=>!catFilter || s.cat===catFilter)
    .sort((a,b)=>{
      const k=sort.key;
      if(k==='q') return a.q.localeCompare(b.q)*sort.dir;
      if(k==='cat') return (a.cat.localeCompare(b.cat)||b.avg-a.avg)*sort.dir;
      return (a[k]-b[k])*sort.dir;
    });

  const S = window.RUGBY.staff;
  const open = (field)=> st.rows.map(r=>({ev:r.ev, txt:r[field]})).filter(o=>o.txt && o.txt.trim());

  return (
    <div className="stack fade-in">

      {/* KPIs por categoría */}
      <section>
        <SectionHead title="Promedio por dimensión" hint={`${st.evaluadores.length} evaluadores · escala 1–4`}
          right={<span className="zbadge" style={{background:'var(--panel-3)',color:'var(--text-2)'}}>
                   Global <b style={{color:zoneOf(st.overall,st.cfg).color,marginLeft:5}}>{r1(st.overall)}</b></span>}/>
        <div className="grid" style={{gridTemplateColumns:'repeat(4,1fr)'}}>
          {st.catStats.map(c=>(
            <KpiCard key={c.cat} label={c.cat} value={c.avg} cfg={st.cfg}
              sub={CAT_DESC[c.cat]}
              active={catFilter===c.cat}
              onClick={()=>setCatFilter(f=>f===c.cat?null:c.cat)}/>
          ))}
        </div>
        <div style={{fontSize:12,color:'var(--text-4)',marginTop:9,paddingLeft:2}}>
          Tocá una dimensión para filtrar el detalle ↓
        </div>
      </section>

      {/* Insights */}
      <section>
        <SectionHead title="Lectura rápida" hint="calculado a partir de las 17 preguntas"/>
        <div className="grid" style={{gridTemplateColumns:'repeat(3,1fr)'}}>
          <div className="insight">
            <div className="ins-head" style={{color:'var(--verde)'}}><Ico d={ICONS.up} size={16}/>Fortalezas</div>
            {st.fort.map((s,i)=>(
              <InsightItem key={s.q} rank={i+1} name={s.q} sub={s.cat} value={s.avg} cfg={st.cfg}/>
            ))}
          </div>
          <div className="insight">
            <div className="ins-head" style={{color:'var(--rojo)'}}><Ico d={ICONS.down} size={16}/>A trabajar</div>
            {st.debi.map((s,i)=>(
              <InsightItem key={s.q} rank={i+1} name={s.q} sub={s.cat} value={s.avg} cfg={st.cfg}/>
            ))}
          </div>
          <div className="insight">
            <div className="ins-head"><Ico d={ICONS.scale} size={16}/>Consenso del staff</div>
            <div style={{fontSize:11.5,color:'var(--text-4)',letterSpacing:'.06em',textTransform:'uppercase',fontWeight:600,marginBottom:2}}>Mayor acuerdo</div>
            {st.acuerdoMax.map((s)=>(
              <InsightItem key={s.q} name={s.q} value={'±'+r1(s.sd)} accentColor={'var(--verde)'}/>
            ))}
            <div style={{fontSize:11.5,color:'var(--text-4)',letterSpacing:'.06em',textTransform:'uppercase',fontWeight:600,margin:'12px 0 2px'}}>Más dividido</div>
            {st.desacuerdoMax.map((s)=>(
              <InsightItem key={s.q} name={s.q} value={'±'+r1(s.sd)} accentColor={'var(--ambar)'}/>
            ))}
          </div>
        </div>
      </section>

      {/* Detalle por pregunta */}
      <section>
        <SectionHead title="Detalle por pregunta"
          hint={catFilter?`filtrando: ${catFilter}`:'17 indicadores, ordenados por promedio'}
          right={catFilter && <button className="seg" style={{padding:'4px 6px'}}>
            <button className="on" onClick={()=>setCatFilter(null)}>✕ quitar filtro</button></button>}/>
        <div className="card card-pad">
          {Object.keys(S.categorias).filter(c=>!catFilter||c===catFilter).map(cat=>{
            const qs = st.qstats.filter(s=>s.cat===cat).sort((a,b)=>b.avg-a.avg);
            const cAvg = mean(qs.map(q=>q.avg));
            return (
              <div key={cat}>
                <div className="cat-tab">
                  <span className="dot" style={{background:scoreColor(cAvg,st.cfg)}}/>
                  <span>{cat}</span>
                  <span style={{flex:1}}/>
                  <span style={{color:'var(--text-4)',fontWeight:500,fontFamily:'var(--sans)',letterSpacing:0,textTransform:'none'}}>
                    prom <b style={{color:zoneOf(cAvg,st.cfg).color}}>{r1(cAvg)}</b></span>
                </div>
                {qs.map(s=>(<BarRow key={s.q} label={s.q} value={s.avg} cfg={st.cfg}/>))}
              </div>
            );
          })}
          <div style={{display:'flex',justifyContent:'space-between',marginTop:14,paddingTop:10,borderTop:'1px solid var(--line)',fontSize:11.5,color:'var(--text-4)'}}>
            <span>1 · Insuficiente</span><span>2 · En desarrollo</span><span>3 · Sólido</span><span>4 · Destacado</span>
          </div>
        </div>
      </section>

      {/* Tabla completa con per-evaluador */}
      <section>
        <SectionHead title="Tabla completa" hint="promedio, dispersión y voto de cada evaluador"/>
        <div className="card" style={{overflow:'hidden'}}>
          <div style={{overflowX:'auto'}}>
            <table className="dt">
              <thead><tr>
                <Th k="cat" sort={sort} setSort={setSort}>Dimensión</Th>
                <Th k="q" sort={sort} setSort={setSort}>Indicador</Th>
                {st.evaluadores.map(ev=>(<th key={ev} className="num" title="Respuesta anónima" style={{cursor:'default',fontSize:10}}>{ev.replace('Evaluador ','E')}</th>))}
                <Th k="sd" sort={sort} setSort={setSort} num>Disp.</Th>
                <Th k="avg" sort={sort} setSort={setSort} num>Prom.</Th>
              </tr></thead>
              <tbody>
                {visibleQ.map(s=>(
                  <tr key={s.q}>
                    <td style={{color:'var(--text-3)',fontSize:12.5}}>{s.cat}</td>
                    <td className="pname">{s.q}</td>
                    {st.evaluadores.map(ev=>{
                      const v = (st.rows.find(r=>r.ev===ev)||{ratings:{}}).ratings[s.q];
                      return <td key={ev} className="num" style={{padding:'8px 6px'}}>
                        {v==null?<span style={{color:'var(--text-4)'}}>–</span>:
                         <span style={{display:'inline-block',width:22,height:22,lineHeight:'22px',borderRadius:6,
                           background:scoreColor(v,st.cfg),color:'#06120c',fontWeight:700,fontSize:12}}>{v}</span>}
                      </td>;
                    })}
                    <td className="num" style={{color:'var(--text-3)'}}>±{r1(s.sd)}</td>
                    <td className="num">
                      <span className="cellpill" style={{background:zoneOf(s.avg,st.cfg).soft,color:zoneOf(s.avg,st.cfg).color}}>{r1(s.avg)}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>

      {/* Respuestas abiertas */}
      <section>
        <SectionHead title="Respuestas abiertas" hint="comentarios del cuerpo técnico"/>
        <div className="grid" style={{gridTemplateColumns:'1fr 1fr'}}>
          <OpenColumn title="Aprendizajes y avances técnicos/tácticos" cls="good" items={open('aprendizajes')}/>
          <OpenColumn title="Oportunidades de mejora del staff" cls="warn" items={open('mejoras')}/>
        </div>
        <div style={{marginTop:16}}>
          <OpenColumn title="Suma libre" cls="" items={open('suma')} full/>
        </div>
      </section>

    </div>
  );
}

function OpenColumn({title, items, cls, full}){
  return (
    <div>
      <div className="cat-tab" style={{paddingTop:0}}>{title}<span style={{color:'var(--text-4)',marginLeft:4}}>· {items.length}</span></div>
      <div className="grid" style={{gridTemplateColumns:full?'1fr 1fr':'1fr', gap:12}}>
        {items.map((o,i)=>(
          <div key={i} className={'quote '+cls}>
            {o.txt}
            <span className="qby">Respuesta anónima</span>
          </div>
        ))}
      </div>
    </div>
  );
}

Object.assign(window, { StaffView });
