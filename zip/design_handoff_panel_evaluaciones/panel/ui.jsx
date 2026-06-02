/* ============================================================
   ui.jsx — helpers + primitivas compartidas
   ============================================================ */
const { useState, useMemo, useRef, useEffect } = React;

/* ---------- math ---------- */
const mean = a => a.length ? a.reduce((s,x)=>s+x,0)/a.length : 0;
const r1 = n => (Math.round(n*10)/10).toFixed(1);
const r2 = n => (Math.round(n*100)/100).toFixed(2);
const stdev = a => { if(a.length<2) return 0; const m=mean(a); return Math.sqrt(mean(a.map(x=>(x-m)**2))); };

/* ---------- scales / semáforo ---------- */
// cfg: {min,max,cuts:[rojo|ámbar, ámbar|sólido, sólido|destacado]}
const SCALE_IND  = { min:1, max:3, cuts:[1.67, 2.33, 2.67] };
const SCALE_STAFF= { min:1, max:4, cuts:[1.8, 2.7, 3.5] };

const ZONES = {
  riesgo:    { label:'En riesgo',   color:'var(--rojo)',  soft:'var(--rojo-soft)',  raw:[240,84,79] },
  desarrollo:{ label:'En desarrollo',color:'var(--ambar)', soft:'var(--ambar-soft)', raw:[242,178,62] },
  solido:    { label:'Sólido',      color:'var(--verde)', soft:'var(--verde-soft)', raw:[63,191,127] },
  destacado: { label:'Destacado',   color:'var(--verde)', soft:'var(--verde-soft)', raw:[63,191,127] },
};
function zoneKey(v, cfg){
  if(v < cfg.cuts[0]) return 'riesgo';
  if(v < cfg.cuts[1]) return 'desarrollo';
  if(v < cfg.cuts[2]) return 'solido';
  return 'destacado';
}
function zoneOf(v,cfg){ return { key:zoneKey(v,cfg), ...ZONES[zoneKey(v,cfg)] }; }

// continuous heatmap color anchored to cuts (red→amber→green)
function lerp(a,b,t){ return a.map((x,i)=>Math.round(x+(b[i]-x)*t)); }
const C_ROJO=[240,84,79], C_AMBAR=[242,178,62], C_VERDE=[63,191,127], C_DEEP=[46,168,108];
function scoreColor(v,cfg){
  const {min,max,cuts}=cfg;
  let p;
  if(v<=cuts[0]) p = 0.16*(v-min)/Math.max(0.001,(cuts[0]-min));
  else if(v<=cuts[1]) p = 0.16 + 0.42*(v-cuts[0])/(cuts[1]-cuts[0]);
  else p = 0.58 + 0.42*(v-cuts[1])/Math.max(0.001,(max-cuts[1]));
  p=Math.max(0,Math.min(1,p));
  let rgb;
  if(p<0.5) rgb=lerp(C_ROJO,C_AMBAR,p/0.5);
  else if(p<0.82) rgb=lerp(C_AMBAR,C_VERDE,(p-0.5)/0.32);
  else rgb=lerp(C_VERDE,C_DEEP,(p-0.82)/0.18);
  return `rgb(${rgb[0]},${rgb[1]},${rgb[2]})`;
}

/* ---------- tiny icons ---------- */
const Ico = ({d,size=18,sw=1.7,fill=false}) => (
  <svg className="ni-ico" width={size} height={size} viewBox="0 0 24 24" fill={fill?'currentColor':'none'}
       stroke="currentColor" strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round">{d}</svg>
);
const ICONS = {
  staff: <><path d="M3 21h18"/><path d="M5 21V8l7-4 7 4v13"/><path d="M9 21v-6h6v6"/></>,
  player: <><circle cx="12" cy="8" r="3.2"/><path d="M5.5 20a6.5 6.5 0 0 1 13 0"/></>,
  bolt: <path d="M13 2 4.5 13H11l-1 9 8.5-11H12l1-9Z"/>,
  up: <path d="M7 14l5-5 5 5"/>,
  down: <path d="M7 10l5 5 5-5"/>,
  info: <><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></>,
  search: <><circle cx="11" cy="11" r="7"/><path d="M21 21l-4-4"/></>,
  target: <><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.4"/></>,
  flag: <><path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5"/></>,
  spark: <path d="M12 3v3m0 12v3M3 12h3m12 0h3M5.6 5.6l2.1 2.1m8.6 8.6 2.1 2.1m0-12.8-2.1 2.1M7.7 16.3l-2.1 2.1"/>,
  scale: <><path d="M12 3v18"/><path d="M7 8h10"/><path d="m7 8-3 6a3 3 0 0 0 6 0Z"/><path d="m17 8-3 6a3 3 0 0 0 6 0Z"/></>,
};

/* ---------- primitives ---------- */
function SectionHead({title, hint, right}){
  return (
    <div className="sec-head">
      <span className="sec-title">{title}</span>
      {hint && <span className="sec-hint">{hint}</span>}
      <span className="sec-rule"/>
      {right}
    </div>
  );
}

function ZoneBadge({v, cfg, showLabel=true}){
  const z = zoneOf(v,cfg);
  return (
    <span className="zbadge" style={{background:z.soft, color:z.color}}>
      <span className="dot" style={{background:z.color}}/>
      {showLabel && z.label}
    </span>
  );
}

function Meter({v, cfg}){
  const pct = Math.max(3, ((v-cfg.min)/(cfg.max-cfg.min))*100);
  const z = zoneOf(v,cfg);
  return <div className="kpi-meter"><i style={{width:pct+'%', background:z.color}}/></div>;
}

function KpiCard({label, value, cfg, sub, onClick, active}){
  const z = zoneOf(value,cfg);
  return (
    <div className="kpi" onClick={onClick}
         style={{cursor:onClick?'pointer':'default', borderColor:active?'var(--accent-line)':undefined}}>
      <span className="kpi-accent" style={{background:z.color}}/>
      <div className="kpi-lbl">{label}</div>
      {sub && <div style={{fontSize:11,color:'var(--text-4)',marginTop:3,lineHeight:1.3}}>{sub}</div>}
      <div className="kpi-row">
        <span className="kpi-val" style={{color:z.color}}>{r1(value)}</span>
        <span className="kpi-max">/ {cfg.max}</span>
      </div>
      <div className="kpi-zone" style={{color:z.color}}>
        <span className="dot" style={{background:z.color}}/>{z.label}
      </div>
      <Meter v={value} cfg={cfg}/>
    </div>
  );
}

/* distribution bar: counts {Rojo,Amarillo,Verde} or [r,a,v] */
function DistBar({counts}){
  const [r,a,v]=counts; const tot=r+a+v||1;
  return (
    <div className="distbar" title={`Rojo ${r} · Amarillo ${a} · Verde ${v}`}>
      {r>0 && <span style={{width:(r/tot*100)+'%',background:'var(--rojo)'}}/>}
      {a>0 && <span style={{width:(a/tot*100)+'%',background:'var(--ambar)'}}/>}
      {v>0 && <span style={{width:(v/tot*100)+'%',background:'var(--verde)'}}/>}
    </div>
  );
}

/* bar row for "detalle por pregunta" */
function BarRow({label, value, cfg, dispersion}){
  const z=zoneOf(value,cfg);
  const pct=((value-cfg.min)/(cfg.max-cfg.min))*100;
  return (
    <div className="barrow">
      <div className="bl">{label}</div>
      <div className="bartrack">
        <div className="barfill" style={{width:Math.max(2,pct)+'%',background:scoreColor(value,cfg)}}/>
      </div>
      <div className="barval" style={{color:z.color}}>{r1(value)}</div>
    </div>
  );
}

function Note({children}){
  return <div className="note"><Ico d={ICONS.info} size={15}/><div>{children}</div></div>;
}

/* insight list item */
function InsightItem({rank, name, sub, value, cfg, accentColor}){
  return (
    <div className="ins-item">
      {rank!=null && <span className="ins-rank">{rank}</span>}
      <div style={{flex:1,minWidth:0}}>
        <div className="ins-name">{name}</div>
        {sub && <div className="ins-sub">{sub}</div>}
      </div>
      <span className="ins-val" style={{color: accentColor || (cfg?zoneOf(value,cfg).color:'var(--text)')}}>
        {typeof value==='number'?r1(value):value}
      </span>
    </div>
  );
}

/* sortable header cell */
function Th({children, k, sort, setSort, num}){
  const active = sort.key===k;
  return (
    <th className={num?'num':''} onClick={()=>setSort(s=>({key:k, dir:s.key===k?-s.dir:(num?-1:1)}))}>
      {children}{active && <span className="arr">{sort.dir>0?'▲':'▼'}</span>}
    </th>
  );
}

Object.assign(window, {
  useState, useMemo, useRef, useEffect,
  mean, r1, r2, stdev, SCALE_IND, SCALE_STAFF, ZONES, zoneKey, zoneOf, scoreColor,
  Ico, ICONS, SectionHead, ZoneBadge, Meter, KpiCard, DistBar, BarRow, Note, InsightItem, Th,
});
