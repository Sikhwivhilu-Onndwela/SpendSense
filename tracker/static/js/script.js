document.addEventListener('DOMContentLoaded', () => {

  const cards = document.querySelectorAll(
    '.feat-card, .stat-box, .tip-card, .value-card'
  );

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(24px)';
    card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(card);
  });

  
  const progressFill = document.querySelector('.progress-fill');
  if (progressFill) {
    const targetWidth = progressFill.style.width;
    progressFill.style.width = '0%';
    setTimeout(() => {
      progressFill.style.width = targetWidth;
    }, 300);
  }

  
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-links a');
  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

});