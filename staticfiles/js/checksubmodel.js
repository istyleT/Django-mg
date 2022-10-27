const checksubmodel = document.getElementById('checksubmodel');
checksubmodel.addEventListener("click", function(e) {
     const submodel = document.getElementsByName('submodel');
     
     if (submodel.value  == "-"){
          e.preventDefault();
          document.getElementById('error-queryprice').style.display = 'block';
     }
});