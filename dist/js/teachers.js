let moreText=document.getElementById("hidden-text");
let moreBlock=document.getElementById("div1");
function down() {
    if(moreText.style.display="none"){
        moreText.style.display="block";
        moreBlock.style.height="350px";
        document.getElementById("button1").style.display="none";
        document.getElementById("button2").style.display="block";
    }
        
  };
  function up() {
  if(moreText.style.display="block"){
    moreText.style.display="none";
    moreBlock.style.height="200px";
    document.getElementById("button2").style.display="none";
        document.getElementById("button1").style.display="block";
}
  };