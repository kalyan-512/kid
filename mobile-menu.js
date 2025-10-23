// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
  // Create mobile menu toggle button
  const header = document.querySelector('.header__inner');
  const nav = document.querySelector('.nav');
  
  if (header && nav) {
    // Create overlay
    const overlay = document.createElement('div');
    overlay.className = 'mobile-menu-overlay';
    document.body.appendChild(overlay);
    
    // Create toggle button
    const toggleBtn = document.createElement('button');
    toggleBtn.className = 'mobile-menu-toggle';
    toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
    toggleBtn.setAttribute('aria-label', 'Toggle mobile menu');
    
    // Insert before nav
    header.insertBefore(toggleBtn, nav);
    
    // Toggle menu on click
    toggleBtn.addEventListener('click', function() {
      nav.classList.toggle('active');
      overlay.classList.toggle('active');
      
      // Change icon
      const icon = toggleBtn.querySelector('i');
      if (nav.classList.contains('active')) {
        icon.className = 'fas fa-times';
        document.body.style.overflow = 'hidden'; // Prevent scrolling
      } else {
        icon.className = 'fas fa-bars';
        document.body.style.overflow = '';
      }
    });
    
    // Close menu when clicking overlay
    overlay.addEventListener('click', function() {
      nav.classList.remove('active');
      overlay.classList.remove('active');
      toggleBtn.querySelector('i').className = 'fas fa-bars';
      document.body.style.overflow = '';
    });
    
    // Close menu on link click
    const navLinks = nav.querySelectorAll('.nav__link');
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        nav.classList.remove('active');
        overlay.classList.remove('active');
        toggleBtn.querySelector('i').className = 'fas fa-bars';
        document.body.style.overflow = '';
      });
    });
  }
});
