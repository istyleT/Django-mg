var submodelid = document.getElementById('submodelid');
var formsubmodel = document.getElementById("formsubmode");
var errorsubmodel = document.getElementById("errorsubmodel");

formsubmodel.addEventListener("submit", (e)=> {
                    let box = []
                    if (submodelid.value === "" || submodelid.value == null) {
                       box.push('กรุณาเลือกรุ่นย่อย')       
                    }
                    if (box.length > 0) {
                                        e.preventDefault(); 
                                        errorsubmodel.innerHTML = box.join('');
                                        document.getElementById("errorsubmodel").className = 'alert alert-danger'; 
                    }        
});