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





function addacc() {
     let test = document.querySelectorAll('[type="checkbox"]');
     acc_sum = 0 ;
     for ( chk in test ) {
          if (chk.checked) {
               acc_sum += test.value;
               console.log(acc_sum) ;
          }
          else {
               console.log('None')
          }
     }
        
}
