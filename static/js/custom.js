const username = document.getElementById("username");
const telnumber = document.getElementById("telnumber");
const mainmodel = document.getElementById("mainmodel");
const form = document.getElementById("form");
const errormessage = document.getElementById("error");


form.addEventListener("submit", (e)=> {
                    let box = []
                    if (username.value === "" || username.value == null) {
                       box.push('กรุณากรอกชื่อผู้ใช้งาน')       
                    }
                    if (telnumber.value === "" || telnumber.value == null ){
                        box.push('กรุณากรอกเบอร์ติดต่อ')  
                    } 
                    if (mainmodel.value == 'N'){
                         box.push('กรุณาเลือกรุ่นรถ')           
                    } 
                    if (box.length > 0) {
                                        e.preventDefault(); 
                                        console.log('error')
                                        errormessage.innerHTML = box.join(',');
                                        document.getElementById("error").className = 'alert alert-danger'; 
                    }

     
      
              
});

