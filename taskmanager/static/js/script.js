const MAIN_NAV = document.getElementsByTagName('nav')[0];
const MAIN_NAV_TOGGLE = document.getElementById('main-nav-toggle');
MAIN_NAV.style.display = 'none';


MAIN_NAV_TOGGLE.addEventListener('click', toggleNav);

function toggleNav() {
    MAIN_NAV.style.display === 'none' ?
        MAIN_NAV.style.display = 'block'
        : MAIN_NAV.style.display = 'none';
}