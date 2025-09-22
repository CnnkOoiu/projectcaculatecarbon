// main.js
// Enhance symmetry and modern UI with JS only for field display logic

document.addEventListener('DOMContentLoaded', function() {
    function showFields() {
        var type = document.getElementById('calc_type').value;
        document.querySelectorAll('.input-group').forEach(e => e.classList.add('hidden'));
        if(type === 'perfect_area') {
            document.getElementById('group-perfect_area').classList.remove('hidden');
        } else if(type === 'radians_index') {
            document.getElementById('group-radians_index').classList.remove('hidden');
        } else if(type === 'ba_carbon') {
            document.getElementById('group-ba_carbon').classList.remove('hidden');
        } else if(type === 'dbh_type') {
            document.getElementById('group-dbh_type').classList.remove('hidden');
        } else if(type === 'allometric') {
            document.getElementById('group-allometric').classList.remove('hidden');
        } else if(type === 'calculate_C') {
            document.getElementById('group-calculate_C').classList.remove('hidden');
        }
    }
    var calcType = document.getElementById('calc_type');
    if (calcType) {
        calcType.addEventListener('change', showFields);
        showFields(); // Initial call for page load
    }
    // Bamboo type field toggle for allometric and calculate_C
    var forestSelects = document.querySelectorAll('select[name="forest"]');
    forestSelects.forEach(function(select) {
        select.addEventListener('change', function() {
            var bambooDiv = select.parentElement.querySelector('div[id^="bamboo_type"]');
            if (select.value == '6') {
                bambooDiv.style.display = 'block';
            } else {
                bambooDiv.style.display = 'none';
            }
        });
    });
});
