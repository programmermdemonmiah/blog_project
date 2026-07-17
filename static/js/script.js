function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-custom ${type}`;

    const iconMap = {
        success: 'fas fa-check-circle',
        error: 'fas fa-exclamation-circle',
        warning: 'fas fa-exclamation-triangle',
        info: 'fas fa-info-circle',
    };
    const icon = iconMap[type] || iconMap.info;

    toast.innerHTML = `<i class="${icon}"></i><span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
        if (toast.parentNode) {
            toast.remove();
        }
    }, 3500);
}

document.addEventListener('DOMContentLoaded', function () {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (el) {
        return new bootstrap.Tooltip(el);
    });
});

function slideCategories(direction) {
    const slider = document.getElementById('categoriesSlider');
    if (!slider) return;
    const card = slider.querySelector('.category-slide-card');
    if (!card) return;
    const scrollAmount = card.offsetWidth + 24;
    slider.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
}
