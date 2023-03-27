const username = document.getElementById("username");
const password = document.getElementById("password");
const formlogin = document.getElementById("formlogin");
const errormessage = document.getElementById("error");


formlogin.addEventListener("submit", (e)=> {
                    let box = []
                    if (username.value === "" || username.value == null) {
                       box.push('กรุณากรอกชื่อผู้ใช้งาน')       
                    }
                    if (password.value === "" || password.value == null ){
                        box.push('กรุณากรอกรหัสผ่าน')  
                    } 
                    if (box.length > 0) {
                                        e.preventDefault(); 
                                        console.log('error')
                                        errormessage.innerHTML = box.join(',');
                                        document.getElementById("error").className = 'alert alert-warning'; 
                    }         
});

