function showFunction(fade) {
    const area = document.getElementById(`${fade}`);
    const arrayArea = document.getElementsByClassName('table-content')
    const tab = document.getElementById(`${fade}-id`)
    const navItem = document.getElementsByClassName('nav-item')
    console.log(navItem[1],'6y6t');

    for (let i = 0; i < navItem.length; i++) {
      if(navItem[i].id == tab.id) {
          navItem[i].style.background = 'rgba(14, 35, 56, 0.88)'
          navItem[i].style.color = 'rgba(250, 250, 250, 0.88)'
        }
      else{
        navItem[i].style.background = 'none'
        navItem[i].style.color = 'black'
        

      }
    }

    console.log(tab,'taaaaaab');
    


  console.log(area.id);

  for (let i = 0; i < arrayArea.length; i++) {
      console.log(arrayArea[i].id);
      
      if (area.id == arrayArea[i].id) {
          console.log(true);
          arrayArea[i].style.display = 'block'; 
      }
      else{
          arrayArea[i].style.display = 'none'; 
      }
  }
}