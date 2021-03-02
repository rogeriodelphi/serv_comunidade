let polo  = document.querySelector('#polo');
let select  = document.querySelector('#servicos');

select.addEventListener('change', e=>{
	polo.querySelector('h3 b').textContent = select.value;
	polo.classList.add('active')
})

