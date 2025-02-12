


window.addEventListener('DOMContentLoaded', event => {




    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };
  
    
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });
  
  });
  
  
  function readMore(isReadMoreExpanded,blogId,secondQuoteId,readLessId,readMoreId,blogTitleId){
    console.log(blogId);
  
    const blogTitle = document.getElementById(blogTitleId)
    const blog = document.getElementById(blogId)
  
    const secondQuote = document.getElementById(secondQuoteId)
    const readLess = document.getElementById(readLessId)
    const readMore = document.getElementById(readMoreId)
  
  
    if(isReadMoreExpanded){
        console.log('expanded');
        blog.style.display = 'block';
        blog.style.overflow = 'visible';
        blog.style.whiteSpace = 'normal';
        secondQuote.style.display = 'block';
        readMore.style.display = 'none';
        readLess.style.display = 'block';
        blog.style.transition = 'width 2s';
  
  
        
  
    
    }else{
        blog.style.display = '-webkit-box';
        blog.style.webkitLineClamp= 4;
        blog.style.whiteSpace = 'normal';
        blog.style.overflow = 'hidden';
        blog.style.textOverflow = 'ellipsis';
        blog.whiteSpace = 'normal';
        secondQuote.style.display = 'none';
        readLess.style.display = 'none';
        readMore.style.display = 'block';
        blogTitle.scrollIntoView({ behavior: 'smooth' });
  
        // const rect = blogTitle.getBoundingClientRect();
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        window.scrollTo({
            top: rect.top + scrollTop,
            behavior: 'smooth'
        });
  
  
        
  
  
    }
  
  
  
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  document.addEventListener("DOMContentLoaded", function () {
    let isKeyword = false
    let matchCardFound = false
   const pagination = document.getElementById('paginationId')
   const viewAll = document.getElementById('view-all-button')
   const searchNotFound = document.getElementById('search-not-foundId')
   // Function to show the corresponding element
  
  //  searchNotFound.style.display = 'none';
  // viewAll.style.display = 'none'
  
   function showPage() {
     const url = window.location.href;
     const newURL = new URL(window.location);
  
  
     const urlObj = new URL(url);
  
  
     
     const searchParams = new URLSearchParams(urlObj.search);
     const keyword = searchParams.get('search');
  
     if(keyword?.trim()){
  
       isKeyword = true
       console.log(keyword);
       
       const cards = document.querySelectorAll('.single-amenities');
  
       cards.forEach(card => {
           const categoryName = card.querySelector('.category-name').innerText.toLowerCase().trim();
           
           if (categoryName?.includes(keyword)) {
               // card.style.display = 'block';
               console.log('match found');
               matchCardFound = true;
               console.log(card);
               card.style.display = 'block';
               pagination.style.display = 'none'
               viewAll.style.display = 'block'
               newURL.searchParams.delete('search');
               window.history.pushState({}, '', newURL);
           } else {
           card.style.display = 'none';
          //  searchNotFound.style.display = 'block';
            viewAll.style.display = 'block'
           }
         })
  
     }
  
         const pageNo = url.split("#")[1] ? url.split("#")[1] : "page-1"; // Extract the hash part of the URL
  
     // getting elements from html
     if (pageNo) {
       const pageId = document.getElementById(pageNo);
       const NoId = document.getElementById(pageNo.slice(5));
       const leftId = document.getElementById("left");
       const rightId = document.getElementById("right");
       const lastPageNoClass = document.getElementsByClassName("page-item-last");
       const lastPageNoId = lastPageNoClass[0];
       const nextElement1 = NoId.nextElementSibling;
       const previousElement1 = NoId.previousElementSibling;
       const pageNoDotsId = document.getElementById("pageno-dots");
  
       // Hide all pages
       document.querySelectorAll('div[id^="page-"]').forEach((div) => {
         div.style.display = "none";
       });
  
       // Check if the element exists and then show it
       if (pageId) {
         pageId.style.setProperty("display", "block", "important");
         window.scrollTo({
           top: 0,
           // behavior: "smooth",
         });
  
         // Hiding page numbers
         document.querySelectorAll(".page-item").forEach((div) => {
           div.style.display = "block";
           div.style.display = "none";
           div.classList?.remove("active");
           lastPageNoId.classList.remove("active");
         });
         if (lastPageNoId !== NoId) NoId?.classList?.add("active");
  
         // handling previous element and next element.
         if (previousElement1 && nextElement1) {
           if (
             nextElement1.id != pageNoDotsId.id &&
             previousElement1.id != pageNoDotsId.id
           ) {
             nextElement1.style.display = "block";
             previousElement1.style.display = "block";
           } else {
             previousElement1.style.display = "block";
           }
           NoId.style.display = "block";
         }
  
         // for hiding left and right arrows on starting and ending.
         if (pageNo.slice(5) == "1") {
           leftId.style.display = "none";
           rightId.style.display = "block";
         } else if (pageNo.slice(5) == lastPageNoId.id) {
           rightId.style.display = "none";
           leftId.style.display = "block";
         } else {
           leftId.style.display = "block";
           rightId.style.display = "block";
         }
       } else {
         console.error("Element with ID " + pageNo + " not found.");
       }
  
       // handling last page element
       if (
         +NoId.id == +lastPageNoId.id ||
         +NoId.id + 1 == +lastPageNoId.id ||
         +NoId.id + 2 == +lastPageNoId.id
       ) {
         pageNoDotsId.style.setProperty("display", "none", "important");
         const scndLastElement = document.getElementById(NoId.id - 1);
         const prevScndLastElement = document.getElementById(NoId.id - 2);
         if (+NoId.id == +lastPageNoId.id) {
           scndLastElement.style.display = "block";
           prevScndLastElement.style.display = "block";
           NoId.classList.add("active");
         }
       } else {
         pageNoDotsId.style.display = "block";
       }
  
      //  if(keyword){
      //    pagination.style.display = 'none'
      //    viewAll.style.display = 'block'
      //   console.log('show view all');
  
      //  }else{
      //   console.log('show pagination...');
      //    pagination.style.display = 'block'
      //    viewAll.style.display = 'none'
      //    searchNotFound.style.display = 'none'
  
      //  }
      //  if(matchCardFound){
      //   pagination.style.display = 'none'
      //    viewAll.style.display = 'block'
      //    searchNotFound.style.display = 'none'
  
      //  }
  
  
     } else {
       console.log("Error");
     }
   }
  
   // Initial call to show the page when the document is loaded
   showPage();
  
   // Listen for hash changes in the URL
   window.addEventListener("hashchange", showPage);
  });
  
  function handleDirection(direction) {
   const currentUrl = window.location.href;
   const pageNo = currentUrl.split("#")[1]
     ? currentUrl.split("#")[1].slice(5)
     : "page-1".slice(5); // Extract the hash part of the URL
  
   if (pageNo) {
     console.log("this is pageNo:", pageNo);
   }
  
   if (direction == "left") {
     window.location.hash = `#page-${+pageNo - 1}`;
   } else if (direction == "right") {
     window.location.hash = `#page-${+pageNo + 1}`;
   }
  
   // Reload the page
   window.location.reload();
  }
  
  function handleDirectionWithPageNo(pageNo){
  
  window.location.hash =`#page-${pageNo}`;
  window.location.reload();
  
  }
  
  
  // handling sidebar fixed property...
  
  $(function () {
   var top =
     $("#sidebar").offset().top -
     parseFloat($("#sidebar").css("marginTop").replace(/auto/, 0));
   var footTop =
     $("#footer-starting").offset().top -
     parseFloat($("#footer-starting").css("marginTop").replace(/auto/, 0));
  
   var maxY = footTop - $("#sidebar").outerHeight();
  
   console.log($("#sidebar").outerHeight(),'hahahahah....');
  
   $(window).scroll(function (evt) {
     var y = $(this).scrollTop();
     if (y >= top - $("#mainNav").height()) {
       if (y < maxY) {
         $("#sidebar").addClass("fixed").removeAttr("style");
         // $("#sidebar").css({t})
       } else {
         $("#sidebar")
           .removeClass("fixed")
           .css({
             position: "absolute",
             top: maxY - top + "px"
           });
       }
     } else {
       $("#sidebar").removeClass("fixed");
     }
   });
  });
  
  
  // code for modal...
  
  function cancelModal() {
   $("#largeModal").modal("hide");
  }
  
  function showLargeModal(cat,img, title, description) {
    console.log(img,'fgggggggggg');
    
   const modalContent = `
   <div class="blog_area single-post-area">
     <div class="">
        <div onclick="cancelModal()" class="cancelButton"><i class="fa fa-times" style="font-size: larger;" aria-hidden="true"></i>
         </div>
         <div class="main_blog_details">
           <img class="img-fluid" src="${img}" alt="">
             <h4>${title}</h4>
           <div class="user_details">
             <div class="catbox">
               <a href="">${cat}</a>
             </div>
             <div class="mt-sm-0 mt-3"></div>
           </div>
           <p>${description}</p>
           
         </div>
         <div class="navigation-area"></div>
     </div>
   </div>
  `;
  
   document.getElementById("dynamic-modal-content").innerHTML = modalContent;
   $("#largeModal").modal("show");
  }
  
  
  // reloading...
  
  function reloadPage() {
   location.reload();
  }
  
  
  
  function selectCategory(keyword){
  
  
  
  const pagination = document.getElementById('paginationId')
  const viewAll = document.getElementById('view-all-button')
  const cards = document.querySelectorAll('.single-amenities');
  let searchCard = null
  
  
  
  cards.forEach(card => {
    const categoryName = card.querySelector('.category-name').innerText.toLowerCase().trim();
    
  
    if (categoryName?.includes(keyword)) {
        // card.style.display = 'block';
  
        searchCard = card
        
        console.log('match found');
        console.log(card);
        
        // card.style.display = 'block';
        
       
    } else {
    card.style.display = 'none';
   //  searchNotFound.style.display = 'block';
     viewAll.style.display = 'block'
    }
  })
  
  if(searchCard){
    searchCard.style.display = 'block';
    console.log('logggggg');
    
    pagination.style.display = 'none'
        viewAll.style.display = 'block';
        // newURL.searchParams.delete('search');
        // window.history.pushState({}, '', newURL);
  
  }else{
    searchCard.style.display = 'none';
   //  searchNotFound.style.display = 'block';
     viewAll.style.display = 'block'
    }
  }
  
  
  
  
  
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
      
  
  
  
      // font-size: large;
      // /* padding-top: 15px; */
      // color: #00000073;
      // align-content: center;
  
  
  //     border-radius: 49px;
  //     padding: 5px;
  //     padding-inline: 15px;
  //     /* background: #e7e7e7; */
  //     background: linear-gradient(to right, #188ef4 0%, #316ce8 100%);
  //     color: whitesmoke;
  //     box-shadow: 0px 2px 3px #00000063;
  
  
  function changeTab(role){
  
    const user = document.getElementById('user');
    const customer = document.getElementById('customer');
  
    user.classList.remove('user-class')
    customer.classList.remove('customer-class')
    user.classList.remove('fade-in-right')
    customer.classList.remove('fade-in-left')
    // user.classList.remove('fade-out-right')
    // customer.classList.remove('fade-out-left')
    
    // Resetting the styles
    user.style.borderRadius = '';
    user.style.padding = '0px';
    user.style.paddingInline = '';
    user.style.background = '';
    user.style.color = '';
    user.style.boxShadow = '';
    user.style.fontSize = '';
    user.style.paddingTop = '';
    user.style.alignContent = '';
  
    customer.style.borderRadius = '';
    customer.style.padding = '0px';
    customer.style.paddingInline = '';
    customer.style.background = '';
    customer.style.color = '';
    customer.style.boxShadow = '';
    customer.style.fontSize = '';
    customer.style.paddingTop = '';
    customer.style.alignContent = '';
  
    if(role === 'user'){
      console.log('user.....');
      
      user.classList.add('fade-in-right')
      user.style.borderRadius = '49px';
      user.style.padding = '5px';
      user.style.paddingInline = '15px';
      user.style.background = 'linear-gradient(to right, #188ef4 0%, #316ce8 100%)';
      user.style.color = 'white';
      user.style.boxShadow = '0px 2px 3px #00000063';
  
  
      // customer.style.add('fade-out-left')
      customer.style.fontSize = 'large';
      customer.style.color = '#00000073';
      customer.style.alignContent = 'center';
    
      console.log('customer', customer.style);
      console.log('user',user.style);
    
    } else if (role === 'customer'){
      console.log('customer....');
      
      customer.classList.add('fade-in-left')
      customer.style.borderRadius = '49px';
      customer.style.padding = '5px';
      customer.style.paddingInline = '15px';
      customer.style.background = 'linear-gradient(to right, #188ef4 0%, #316ce8 100%)';
      customer.style.color = 'white';
      customer.style.boxShadow = '0px 2px 3px #00000063';
        
      // user.classList.add('fade-out-right')
      user.style.fontSize = 'large';
      user.style.color = '#00000073';
      user.style.alignContent = 'center';
  
      console.log('customer', customer.style);
      console.log('user',user.style);
    }
  } 
  
  
  
  