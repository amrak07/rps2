function toggleMenu() {
    const menu = document.getElementById('menu');
    const menuToggle = document.getElementById('menu-toggle');
    if (menu.style.left === '-200px') {
        menu.style.left = '0';
        menuToggle.innerHTML = '✕';
    } else {
        menu.style.left = '-200px';
        menuToggle.innerHTML = '☰';
    }
}
