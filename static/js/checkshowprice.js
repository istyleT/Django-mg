const checkshowprice = document.getElementById('checkshowprice');
checkshowprice.addEventListener("click", function(e) {
     const bodycolor = document.getElementById('bodycolor');
     const paytype = document.getElementById('paytype');
     const registype = document.getElementById('registype');
     const mgbranch = document.getElementById('mgbranch');
     if (bodycolor.value  == "" || bodycolor.value == null){
          e.preventDefault();
          document.getElementById('error-bodycolor').style.display = 'block';
     }
     if (paytype.value == "" || paytype.value == null){
          e.preventDefault();
          document.getElementById('error-paytype').style.display = 'block';
     }
     if (registype.value == "N" || registype.value == null){
          e.preventDefault();
          document.getElementById('error-registype').style.display = 'block';
     }
     if (mgbranch.value == "" || mgbranch.value == null){
          e.preventDefault();
          document.getElementById('error-mgbranch').style.display = 'block';
     }
});
