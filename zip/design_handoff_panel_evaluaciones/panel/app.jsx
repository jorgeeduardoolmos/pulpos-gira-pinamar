/* ============================================================
   app.jsx — shell, navegación, filtros
   ============================================================ */

const VIEWS = {
  staff:      { label:'Encuesta al Staff', icon:ICONS.staff,  eyebrow:'Mirada del cuerpo técnico' },
  individual: { label:'Evaluación Individual', icon:ICONS.player, eyebrow:'Desempeño jugador por jugador' },
};
const TRIMESTRES = ['T1','T2','T3','T4'];

function NavItem({id, active, onClick}){
  const v=VIEWS[id];
  return (
    <div className={'nav-item'+(active?' active':'')} onClick={onClick}>
      <Ico d={v.icon} size={18}/>{v.label}
    </div>
  );
}

function App(){
  const [view, setView] = useState('staff');
  const [trimestre, setTrimestre] = useState('T1');
  const avail = window.RUGBY.meta.trimestres;

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="sb-brand">
          <div className="sb-crest">
            <div className="crest">
              <span style={{fontFamily:'var(--display)',fontWeight:700,fontSize:15,color:'var(--accent)',letterSpacing:'.02em'}}>M10</span>
            </div>
            <div>
              <div className="sb-club">Liceo Naval</div>
              <div className="sb-sub">Rugby · Infantiles</div>
            </div>
          </div>
        </div>
        <nav className="sb-nav">
          <div className="sb-navlabel">Evaluaciones</div>
          <NavItem id="staff" active={view==='staff'} onClick={()=>setView('staff')}/>
          <NavItem id="individual" active={view==='individual'} onClick={()=>setView('individual')}/>
        </nav>
        <div className="sb-foot">
          <b>Evaluación de desempeño</b><br/>
          Cuerpo técnico · Uso interno<br/>
          <span style={{display:'inline-flex',alignItems:'center',gap:5,marginTop:6,color:'var(--text-3)'}}>
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="4" y="11" width="16" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>
            Respuestas anónimas
          </span>
        </div>
      </aside>

      <main className="main">
        <header className="topbar">
          <div className="tb-titlewrap">
            <div className="tb-eyebrow">{VIEWS[view].eyebrow}</div>
            <h1 className="tb-title">{VIEWS[view].label}</h1>
          </div>
          <span className="tb-spacer"/>
          <div className="tb-controls">
            <div className="field">
              <span className="field-lbl">Trimestre</span>
              <div className="seg">
                {TRIMESTRES.map(t=>(
                  <button key={t} className={trimestre===t?'on':''} disabled={!avail.includes(t)}
                    title={avail.includes(t)?'':'Sin datos cargados'}
                    onClick={()=>avail.includes(t)&&setTrimestre(t)}>{t}</button>
                ))}
              </div>
            </div>
          </div>
        </header>

        <div className="content">
          {view==='staff' ? <StaffView trimestre={trimestre}/> : <IndividualView trimestre={trimestre}/>}
        </div>
      </main>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App/>);
