function openNav() {
    document.getElementById("nav-sidebar").style.width = "200px";
}

function closeNav() {
    document.getElementById("nav-sidebar").style.width = "0";
}

function toggleMenu() {
    document.getElementById("profileOptions").classList.toggle("open-options");
}


// Get the element with the custom scrollbar
const scrollbar = document.querySelector('.custom-scrollbar');

// Add event listeners to handle scrolling
scrollbar.addEventListener('scroll', () => {
  const scrollTop = scrollbar.scrollTop;
  const scrollHeight = scrollbar.scrollHeight;
  const clientHeight = scrollbar.clientHeight;

  // Calculate the scroll position as a percentage
  const scrollPosition = (scrollTop / (scrollHeight - clientHeight)) * 100;

  // Update the scrollbar thumb position
  const thumb = scrollbar.querySelector('::-webkit-scrollbar-thumb');
  thumb.style.top = `${scrollPosition}%`;
});