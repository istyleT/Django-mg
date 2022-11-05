function caldown() {

     // เก็บค่าเตรียมคำนวณ
     const gen_down_percent = document.getElementById('gen_down_percent').value | 0 ;   //pass      
     const gen_down_bath = document.getElementById('gen_down_bath').value | 0 ; //pass 
     const min_reduce = document.getElementById('idmin_reduce').value | 0; //pass 
     const add_eq = document.getElementById('idadd_eq').value | 0;
     const productprice = document.getElementById('productprice').innerHTML ; //pass 
     //สร้างค่าตัวเเปรเริ่มต้น
     let net_productprice = productprice-min_reduce+add_eq ; //pass
     //เริ่มคำนวณค่า
     if (gen_down_percent != 0 && gen_down_bath == 0) {
                   const down_bath = net_productprice*(gen_down_percent/100)
                   console.log(down_bath) ;
                   document.getElementById('show_down_bath').style.display = "block" ; 
                   document.getElementById('gen_down_bath').style.display = "none" ; 
                   document.getElementById('show_down_bath').innerHTML = down_bath.toFixed(0).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')+' '+'บาท' ; 
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
    
                    
};


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

};


/**********************************function คำนวณดอกเบี้ย******************************************/

function  totalgeninter() {
     /* เก็บค่าตัวเเปร */
     const productprice = Number(document.getElementById('productprice').innerHTML) ; //type int 
     const min_reduce = Number(document.getElementById('idmin_reduce').value || 0); // type int
     const add_eq = Number(document.getElementById('idadd_eq').value || 0);  // type int
     const gen_down_percent = Number(document.getElementById('gen_down_percent').value || 0); //type float 
     const gen_month = Number(document.getElementById('idgen_month').value || 0) ; // type int 
     const gen_inter = Number(document.getElementById('idgen_inter').value || 0) ; // type float


     console.log('ราคารถ ='+ productprice)
     console.log(typeof(productprice))
     console.log('ส่วนลดจากราคา ='+ min_reduce)
     console.log(typeof(min_reduce))
     console.log('บวกหัวค่าอุปกรณ์ ='+ add_eq)
     console.log(typeof(add_eq))
     console.log('% เงินดาวน์ =' + gen_down_percent + '%')
     console.log(typeof(gen_down_percent))
     console.log('จำนวนงวด =' + gen_month)
     console.log(typeof(gen_month))
     console.log('% ดอกเบี้ย =' + gen_inter + '%')
     console.log(typeof(gen_inter))
     
     /* คำนวนค่าที่ต้องการ */
     let net_productprice = productprice - min_reduce + add_eq ;
     const cost_finance = net_productprice * (1-(gen_down_percent/100)) ;
     let total_inter_ture =  cost_finance * (gen_inter/100) * (gen_month /12);
     console.log('ราคารถสุทธิ =' + net_productprice)
     console.log('ยอดจัดไฟเเนนซ์ =' + cost_finance)
     console.log('ดอกเบี้ยทั้งหมด =' + total_inter_ture)
     console.log('------------------------------------')
     return total_inter_ture ;

};
/**********************************************************************************************************/

/**********************************************function คำนวณค่า subsidy ทั้งหมด************************************************************/
function sumSubsidy() {
    
    const productprice = Number(document.getElementById('productprice').innerHTML) ; //type int 
    const min_reduce = Number(document.getElementById('idmin_reduce').value || 0); // type int
    const add_eq = Number(document.getElementById('idadd_eq').value || 0);  // type int
    const gen_down_percent = Number(document.getElementById('gen_down_percent').value || '0'); //type float 
    const gen_month = Number(document.getElementById('idgen_month').value || 0) ; // type int 
    const gen_inter = Number(document.getElementById('idgen_inter').value || 0); // type float
    const min_prosub = Number(document.getElementById('idmin_prosub').value || 0);
    const min_inter = Number(document.getElementById('idmin_inter').value || gen_inter);
    const showtotalsubsidy = document.getElementById('showtotalsubsidy');
    /* คำนวนค่าที่ต้องการ */
    let net_productprice = productprice -min_reduce +add_eq ;
    const cost_finance = net_productprice * (1-(gen_down_percent/100)) ;
    let subsidy_inter = cost_finance * (gen_month/12) * ((gen_inter/100)-(min_inter/100));
    let total_subsidy = parseInt(min_prosub + subsidy_inter).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    showtotalsubsidy.style.display = 'block';
    document.getElementById('showtotalsubsidy').innerHTML = total_subsidy + ' ' + 'บาท';
    console.log('--------')
    console.log(min_inter)
    console.log('โปรซับ ='+ min_prosub)
    console.log('ดอกเบี้ยเสนอลูกค้า ='+ min_inter + '%')
    console.log('ซับดอกลูกค้า ='+ subsidy_inter)
    console.log('Subsidy ทั้งหมด ='+ total_subsidy)
    return total_subsidy;

};



/**********************************************************************************************************/



     


