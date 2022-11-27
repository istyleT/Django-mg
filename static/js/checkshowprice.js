function checkcondition(){
  const bodycolor = document.getElementById('bodycolor').value;
  const paytype = document.getElementById('paytype').value;
  const registype = document.getElementById('registype').value;
  const mgbranch = document.getElementById('mgbranch').value;
  const appendbtn = document.getElementById('append-btn');
  
  if (bodycolor != "-" && paytype != "-" && registype != "N" && mgbranch != "-"){
       appendbtn.style.display = 'block';
  }
  else{
       appendbtn.style.display = 'none';
  }  
  return
};
