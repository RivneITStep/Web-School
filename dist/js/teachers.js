// let moreText = document.getElementById("hidden-text");
// // let moreBlock=document.getElementById("div1");
// let btnToggle = document.querySelector("#button1");
// btnToggle.addEventListener("click", down);

// function down(btnToggle) {
//   console.log("This = > ", btnToggle);
//   if ((moreText.style.display = "none")) {
//     moreText.style.display = "block";
//     // moreBlock.style.height="370px";
//     document.getElementById("button1").style.display = "none";
//     document.getElementById("button2").style.display = "block";
//   }
// }
// function up() {
//   console.log("This = > ", this);
//   if ((moreText.style.display = "block")) {
//     moreText.style.display = "none";
//     // moreBlock.style.height="200px";
//     document.getElementById("button2").style.display = "none";
//     document.getElementById("button1").style.display = "block";
//   }
// }
$(document).ready(function() {
  $("button").click(function() {
    $(".hid").toggle(this);
  });
});
// if ($(this).val() == "Детальніше") {
//   $(".hid").toggle();
//   $(this).val("Згорнути");
// } else {
//   $(".hid").toggle();
//   $(this).val("Детальніше");
// }
