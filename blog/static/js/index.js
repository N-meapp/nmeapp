document.addEventListener("DOMContentLoaded", function (){
    const cardArray = document.getElementsByClassName('item')

    let flag=0


    for(let i=0;i<cardArray.length;i++){
     

        setTimeout(() => {
            if(cardArray[i].classList.contains('active')){

                cardArray[i].classList.remove('')

                
                
            }else{
                cardArray[i].classList.add('active')
                
                
            }
        }, i*200);
        
        
    }

  


    setInterval(function(){

        for(let i=0;i<cardArray.length;i++){
            // console.log('first',first[i]);
            // console.log('second',second[i]);

            setTimeout(() => {
                if(cardArray[i].classList.contains('active')){

                    cardArray[i].classList.remove('active')

                    
                    
                }else{
                    cardArray[i].classList.add('active')
                    
                    
                }
            }, i*200);
            
            
        }

    },5000)


    
  })



// /  NEW HEADER   / 



// 






// function showFAQ(sectionId, element) {  
//     // Show the relevant FAQ section
//     document.querySelectorAll('.faq-section').forEach(section => {
//         section.classList.add('hidden');
//     });
//     document.getElementById(sectionId).classList.remove('hidden');

//     // Highlight the active link
//     const links = document.querySelectorAll('.detail a');
//     links.forEach(link => {
//         link.classList.remove('text-blue-600', 'font-bold'); // Remove active styles
//         link.classList.add('text-gray-500'); // Reset to default style
//     });
//     element.classList.remove('text-gray-500'); // Remove default style
//     element.classList.add('text-blue-600', 'font-bold'); // Add active styles
// }

//dropdown control


function controlDropdown(questionNo){

    let  questionArray = ['first answer','secondAnswer', 'third Answer','fourth answer']
    
  
    const faqFooter = document.getElementsByClassName('faq-section')
    const specificQuestion = document.getElementById(questionNo)
    const ansBox = specificQuestion.querySelector('.ansbox')
    const dropDown = specificQuestion.querySelector('.dropdown')
    const pTag = ansBox.querySelector('p')
    
    const allQuestions = document.getElementsByClassName('allquestions')
    
    let x = -1
    let y = -1
    for(let i=0; i<allQuestions.length;i++){
  
     let prevAnsBox =  allQuestions[i].querySelector('.ansbox');
     let prevDropDown = allQuestions[i].querySelector('.dropdown');
     let prevPTag = prevAnsBox.querySelector('p')
  
      if(prevAnsBox.style.height=='40%'){
          console.log('dcreasing height',i);
          x=i;
        setTimeout(() => {
          prevPTag.textContent = '';
        }, 100);
        prevAnsBox.style.height = '0%';
        prevAnsBox.style.padding= '0px';
        prevDropDown.style.transform = 'rotate(0deg)';
  
      }
      if(questionNo.includes(i)){
        console.log('Increasing height',i);
        y=i
        // console.log('haiiii',prevAnsBox,ansBox);
        //   console.log(questionNo,'ddfdfdddddddddddd');
        // setTimeout(() => {
          pTag.textContent = questionArray[i];
        // }, 1000);
        ansBox.style.height = '40%';
        ansBox.style.padding= '25px';
        dropDown.style.transform = 'rotate(180deg)';
        faqFooter[0].style.marginTop = '300px';
        
  
      }
    }
    if(x==y){
      setTimeout(() => {
        prevPTag.textContent = '';
      }, 500);
      ansBox.style.height = '0%';
      ansBox.style.padding= '0px';
      dropDown.style.transform = 'rotate(0deg)';
      faqFooter[0].style.marginTop = '150px';
    }
  }
    
  