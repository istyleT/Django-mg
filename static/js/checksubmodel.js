function appendbutton(){
   const append = document.getElementById("append-btn");
   const submodelid = document.getElementById("submodelid").value;
   console.log(submodelid);
   if ( submodelid !== "-") {
     append.style.display = "block";
   }
   else {
     append.style.display = "none";
   }
   return
} 