
  function changepic() {
    console.log('changepic()ทำงาน');
    /*ค่าที่จะเปลี่ยน*/
    /*var colorcard = document.getElementById('color-card');*/
    const choosemainmodel = String(document.getElementById('2').innerHTML) ; //type int  
    const cardimage = document.getElementById('card-image');
    /*const btnstatus = document.getElementById('btn-status');*/
    /*const att = document.createAttribute("src");*/
    /* ค่าที่จะทำเงื่อนไข mainmodel คุม images / status คุมขอบ เเละ สีปุ่ม*/
    console.log(choosemainmodel);
    /*const choosestatus = "TD";*/
    /*เงื่อนไขการเเสดงผล*/
    switch (choosemainmodel){
      case "MG5" : cardimage.src = "{% static 'picture/Newmg5.png' %}";
      break
      case "MGVSHEV" : cardimage.src = "{% static 'picture/Newmgvshev.png' %}";
      break
      case "MGZS" : cardimage.src = "{% static 'picture/Newmgzs.png' %}";
      break
      case "MGETD" : cardimage.src = "{% static 'picture/Newmgextendergc.png' %}";
      break
      case "MGHSPHEV" : cardimage.src = "{% static 'picture/Newmghs.png' %}";
      break
      case "MGHS" : cardimage.src = "{% static 'picture/Newmghs.png' %}";
      break 
      }
 /*
    switch (choosestatus){
      case "PP" : btnstatus.className = "btn btn-outline-primary";
                  colorcard.style.border = "3px solid #8270ef";
      break
      case "BK" : btnstatus.className = "btn btn-outline-warning";
                  colorcard.style.border = "3px solid #ffde5b";
      break
      case "DV" : btnstatus.className = "btn btn-outline-success";
                  colorcard.style.border = "3px solid #75fb64";
      break
      case "TD" : btnstatus.className = "btn btn-outline-dark";
                  colorcard.style.border = "3px solid #000000";
      break
      case "F" : btnstatus.className = "btn btn-outline-secondary";
                 colorcard.style.border = "3px solid #454944";
      break
    };
   */
    return 
 
   };
