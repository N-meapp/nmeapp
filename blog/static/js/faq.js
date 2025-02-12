function showSection(section, btn) {
    const customerSection = document.getElementById('customer');
    const userSection = document.getElementById('user');
    const custButton = document.getElementById('cust')
    const userButton = document.getElementById('usr')

    
    // Show the appropriate section
    if (section === 'customer') {
        customerSection.classList.remove('hidden');
        userSection.classList.add('hidden');
        custButton.style.background = '#92a0e9'
        userButton.style.background = '#cdcdcd'
        userButton.style.border = '3px solid #c4c1c1'

    
    } else {
        userSection.classList.remove('hidden');
        customerSection.classList.add('hidden');
         custButton.style.background = '#cdcdcd'
        userButton.style.background = '#92a0e9'
        custButton.style.border = '3px solid #c4c1c1'


    }

    
    // Change button styles
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => button.classList.remove('bg-blue-500', 'text-white'));
    btn.classList.add('bg-#2937f0eb', 'text-white');
}

function showFAQ(faqclass,faqId) {
  console.log(faqclass,'faqqqqqqq');
  
    const allFAQs = document.querySelectorAll('.faq-section');
    allFAQs.forEach(faq => faq.classList.add('hidden'));
    
     const selectedFaqs = document.querySelectorAll(`.${faqclass}`);
     selectedFaqs.forEach(faq => faq.classList.remove('hidden'));


        const faqTab = document.getElementById(faqId)
        const deActiveTabs = document.getElementsByClassName('deactive-tab')
        console.log(faqTab,'sdfsfsf');
        

        for(i=0;i<deActiveTabs.length;i++){
            deActiveTabs[i].style.color = 'black'
        }


        faqTab.style.color = 'blue'
    
}

function toggleDropdown(element) {
    const answer = element.nextElementSibling;
    const icon = element.querySelector('.dropdown-icon');

    // Toggle the visibility of the answer
    answer.classList.toggle('hidden');

    // Rotate the dropdown arrow icon
    icon.classList.toggle('rotate-180');
}













function toggleNavbar() {
    const nav = document.getElementById('mobile-nav');
    nav.classList.toggle('hidden');
}

// animation
document.addEventListener('DOMContentLoaded', function() {
    const observerOptions = {
        threshold: 0.1
    };

    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);

    document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right').forEach(element => {
        observer.observe(element);
    });
});


    AOS.init({
        duration: 1000, // Animation duration
        once: true      // Animation happens only once
    });



    function filterCategory(category) {
        console.log("vaaaaaaaaaaa",category)
        // Get all elements with the class 'single-amenities'
        const allCategory = document.getElementsByClassName('single-amenities');
        
        // Get all elements that match the specified category
        const blog = document.getElementsByClassName(category);
    
        // Hide all elements in allCategory
        for (let i = 0; i < allCategory.length; i++) {
            allCategory[i].style.display = 'none';
        }
    
        // Display all elements in blog
        for (let i = 0; i < blog.length; i++) {
            blog[i].style.display = 'block';
        }
    }
    

