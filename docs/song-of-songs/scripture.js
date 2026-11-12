(function(){
var BASE="https://rest.api.bible/v1",
    IDS={NIV:"78a9f6124f344018-01",NASB:"a761ca71e0b3ddcf-01"},
    cells=[].slice.call(document.querySelectorAll('td.raw[data-bible]')),
    key=window.APIBIBLE_KEY,fumsTokens=[],copyrights={},
    credits=document.getElementById('credits-body');
function setAll(msg){cells.forEach(function(c){c.firstChild.textContent=msg;});}
if(!key){setAll("Scripture text unavailable: API.Bible key not configured (see config.js).");return;}
// group cells by version + chapter
var groups={};
cells.forEach(function(c){var g=c.dataset.bible+"|"+c.dataset.ch;(groups[g]=groups[g]||[]).push(c);});
function clean(t){return t.replace(/\s+/g," ").trim();}
function load(g){
  var p=g.split("|"),ver=p[0],ch=p[1],cs=groups[g],
      url=BASE+"/bibles/"+IDS[ver]+"/chapters/SNG."+ch+"?content-type=json&include-notes=false&include-titles=false&include-chapter-numbers=false&include-verse-numbers=true&include-verse-spans=false&fums-version=3";
  return fetch(url,{headers:{"api-key":key}}).then(function(r){if(!r.ok)throw new Error(r.status);return r.json();})
  .then(function(j){
    var d=j.data||{},verses={};
    // walk the content tree: verse text carries attrs.verseId (e.g. SNG.1.2)
    (function walk(n){
      if(!n)return;
      if(Array.isArray(n)){n.forEach(walk);return;}
      if(n.type==="text"&&n.attrs&&n.attrs.verseId){var m=/\.(\d+)$/.exec(n.attrs.verseId);if(m)verses[m[1]]=(verses[m[1]]||"")+" "+n.text;return;}
      walk(n.items);
    })(d.content);
    cs.forEach(function(c){c.firstChild.textContent=clean(verses[c.dataset.v]||"(verse text not returned)");});
    if(j.meta&&j.meta.fumsToken)fumsTokens.push(j.meta.fumsToken);
    if(d.copyright)copyrights[ver]=d.copyright;
  }).catch(function(e){cs.forEach(function(c){c.firstChild.textContent="Scripture text could not be loaded ("+e.message+").";});});
}
Promise.all(Object.keys(groups).map(load)).then(function(){
  if(fumsTokens.length&&window.fums)window.fums('trackView',fumsTokens);
  var names={NIV:"NIV",NASB:"NASB"},html=Object.keys(copyrights).map(function(v){
    return '<p><b>'+names[v]+':</b> '+copyrights[v].replace(/</g,"&lt;")+'</p>';}).join("");
  credits.innerHTML=html+'<p>Scripture provided via <a href="https://api.bible" style="color:var(--accent)">API.Bible</a>.</p>';
});
})();
