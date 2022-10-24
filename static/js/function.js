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



let accPrice = document.getElementById('btn-accpprice'); //ใช้ form ซ้อนกันไม่ได้
accPrice.addEventListener('click', function(e){
     let sumPriceAcc = 0 ;
     e.preventDefault();
     let chk = document.getElementsByName('listacc');
     for (let x ; x < chk.length ; x++){
       if(chk[x].checked == true){
           sumPriceAcc += chk[x].value;
           console.log('sumPriceAcc');
       }
     }
     
});







function caldown() {

     // เก็บค่าเตรียมคำนวณ
     const gen_down_percent = document.getElementById('gen_down_percent').value | 0 ;   //pass      
     const gen_down_bath = document.getElementById('gen_down_bath').value | 0 ; //pass 
     const min_reduce = document.getElementById('min_reduce').value | 0; //pass 
     const productprice = document.getElementById('productprice').innerHTML ; //pass 
     console.log(gen_down_percent) ; 
     console.log(gen_down_bath) ; 
     console.log(min_reduce) ; 
     console.log(productprice) ; 
     //สร้างค่าตัวเเปรเริ่มต้น
     let net_productprice = productprice-min_reduce ; //pass
     console.log(net_productprice) ; 
     //เริ่มคำนวณค่า
     if (gen_down_percent != 0 && gen_down_bath == 0) {
                   const down_bath = net_productprice*(gen_down_percent/100)
                   console.log(down_bath) ;
                   document.getElementById('show_down_bath').style.display = "block" ; 
                   document.getElementById('gen_down_bath').style.display = "none" ; 
                   document.getElementById('show_down_bath').innerHTML = down_bath.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')+' '+'บาท' ; 
                   document.getElementById('downerror').style.display = "none";
        }

     else if (gen_down_percent == 0 && gen_down_bath != 0){
                   const down_percent = (gen_down_bath*100)/net_productprice;
                   console.log(down_percent);
                   document.getElementById('show_down_percent').style.display = "block" ; 
                   document.getElementById('gen_down_percent').style.display = "none" ; 
                   document.getElementById('show_down_percent').innerHTML = down_percent.toFixed(2)+' '+'%';  
                   document.getElementById('downerror').style.display = "none";
     }

     else if (gen_down_percent != 0 && gen_down_bath != 0) {
                 document.getElementById('downerror').style.display = "block";
     }
    
                    
}


function resetdown(){
     
     let a = document.getElementById('show_down_bath') ;
     let b = document.getElementById('gen_down_bath') ;
     let c = document.getElementById('show_down_percent') ;
     let d = document.getElementById('gen_down_percent') ;
     let error = document.getElementById('downerror');

     // ตั้งค่าการเเสดงผล
     a.style.display = "none" ;
     b.style.display = "block" ;
     c.style.display = "none" ;
     d.style.display = "block" ;
     error.style.display = "none" ;

     // ตั้งค่าเริ่มต่น
     b.value = "" ;
     d.value = "" ;

}