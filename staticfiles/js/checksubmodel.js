function ajaxmodel() { 
  let submodel = document.getElementById('submodelid').value;
  console.log(submodel);
  axios ({
    url: '',
    method: 'get',
    params: {'submodel': submodel},
    timeout: 5000,
    headers: {'X-Requested-With': 'XMLHttpRequest'},
  })
  .then (response => {
     let productprice = response.data.productprice;
     document.getElementById('show-price').style.display = 'block';
     document.getElementById('product-price').innerHTML = (productprice.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','));
  })
  .catch(error => {
    alert('เกิดข้อผิดพลาดกรุณาเลือก Grade อีกครั้ง');
  });
  appendbutton();
}
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