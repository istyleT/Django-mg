const submodel = document.getElementsByName("submodel");
const formsubmodel = document.getElementById("formsubmode");
const errorsubmodel = document.getElementById("errorsubmodel");

form.addEventListener("submit", (e)=> {
                    let box = []
                    if (submodel.value === "" || submodel.value == null) {
                       box.push('กรุณาเลือกรุ่นย่อย')       
                    }
                    if (box.length > 0) {
                                        e.preventDefault(); 
                                        errorsubmodel.innerHTML = box.join('');
                                        document.getElementById("errorsubmodel").className = 'alert alert-danger'; 
                    }        
});