// Estado de la aplicación
let compareFractionsArray = [];
let sortFractionsArray = [];

// Cambiar pestañas
function switchTab(tabName) {
    // Ocultar todas las pestañas
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.remove('active');
    });

    // Mostrar la pestaña seleccionada
    document.getElementById(tabName).classList.add('active');
    event.target.classList.add('active');
}

// Función para realizar cálculos
async function calculate() {
    console.log("Boton calcular presionado")
    const fraction1 = document.getElementById('fraction1').value.trim();
    const fraction2 = document.getElementById('fraction2').value.trim();
    const operation = document.getElementById('operation').value;

    if (!fraction1 || !fraction2) {
        showResult('calc-result', 'Por favor, ingresa ambas fracciones', true);
        return;
    }

    try {
        const response = await fetch('/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                action: 'calculate',
                fraction1: fraction1,
                fraction2: fraction2,
                operation: operation
            })
        });

        const data = await response.json();

        if (data.success) {
            const resultHtml = `
                        <div class="result">
                            <h3>Resultado</h3>
                            <div class="result-value">${data.fraction1} ${data.operation} ${data.fraction2} = ${data.result}</div>
                            <div class="result-decimal">Decimal: ${data.decimal}</div>
                        </div>
                    `;
            document.getElementById('calc-result').innerHTML = resultHtml;
        } else {
            showResult('calc-result', data.error, true);
        }
    } catch (error) {
        showResult('calc-result', 'Error de conexión: ' + error.message, true);
    }
}

// Agregar fracción a las listas
function addFraction(type) {
    const inputId = type === 'compare' ? 'compare-fraction' : 'sort-fraction';
    const fraction = document.getElementById(inputId).value.trim();

    if (!fraction) {
        return;
    }

    if (type === 'compare') {
        compareFractionsArray.push(fraction);
        updateFractionList('compare-fractions', compareFractionsArray, 'compare');
    } else {
        sortFractionsArray.push(fraction);
        updateFractionList('sort-fractions', sortFractionsArray, 'sort');
    }

    document.getElementById(inputId).value = '';
}

// Actualizar lista de fracciones
function updateFractionList(containerId, fractions, type) {
    const container = document.getElementById(containerId);
    container.innerHTML = fractions.map((fraction, index) => `
                <div class="fraction-tag">
                    ${fraction}
                    <button class="remove-fraction" onclick="removeFraction(${index}, '${type}')">&times;</button>
                </div>
            `).join('');
}

// Remover fracción
function removeFraction(index, type) {
    if (type === 'compare') {
        compareFractionsArray.splice(index, 1);
        updateFractionList('compare-fractions', compareFractionsArray, 'compare');
    } else {
        sortFractionsArray.splice(index, 1);
        updateFractionList('sort-fractions', sortFractionsArray, 'sort');
    }
}

// Limpiar fracciones
function clearFractions(type) {
    if (type === 'compare') {
        compareFractions = [];
        updateFractionList('compare-fractions', compareFractionsArray, 'compare');
        document.getElementById('compare-result').innerHTML = '';
    } else {
        sortFractionsArray = [];
        updateFractionList('sort-fractions', sortFractionsArray, 'sort');
        document.getElementById('sort-result').innerHTML = '';
    }
}

// Comparar fracciones
async function compareFractions() {
    if (compareFractionsArray.length < 2) {
        showResult('compare-result', 'Se necesitan al menos 2 fracciones para comparar', true);
        return;
    }

    try {
        const response = await fetch('/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                action: 'compare',
                fractions: compareFractionsArray
            })
        });

        const data = await response.json();

        if (data.success) {
            const resultHtml = `
                        <div class="result">
                            <h3>Comparación de Fracciones</h3>
                            <div class="comparison-result">
                                ${data.comparisons.map(item => `
                                    <div class="fraction-item">
                                        <div>
                                            <div class="fraction-value">${item.fraction}</div>
                                            <div class="fraction-info">Decimal: ${item.decimal}</div>
                                        </div>
                                        <div class="position-badge position-${item.position}">${item.position}</div>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    `;
            document.getElementById('compare-result').innerHTML = resultHtml;
        } else {
            showResult('compare-result', data.error, true);
        }
    } catch (error) {
        showResult('compare-result', 'Error de conexión: ' + error.message, true);
    }
}

// Ordenar fracciones
async function sortFractions() {
    if (sortFractionsArray.length < 2) {
        showResult('sort-result', 'Se necesitan al menos 2 fracciones para ordenar', true);
        return;
    }

    const ascending = document.querySelector('input[name="sortOrder"]:checked').value === 'true';

    try {
        const response = await fetch('/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                action: 'sort',
                fractions: sortFractionsArray,
                ascending: ascending
            })
        });

        const data = await response.json();

        if (data.success) {
            const resultHtml = `
                        <div class="result">
                            <h3>Fracciones Ordenadas (${data.order})</h3>
                            <div class="sort-result">
                                ${data.sorted_fractions.map((item, index) => `
                                    <div class="fraction-item">
                                        <div>
                                            <div class="fraction-value">${index + 1}. ${item.fraction}</div>
                                            <div class="fraction-info">Decimal: ${item.decimal}</div>
                                        </div>
                                    </div>
                                `).join('')}
                            </div>
                        </div>
                    `;
            document.getElementById('sort-result').innerHTML = resultHtml;
        } else {
            showResult('sort-result', data.error, true);
        }
    } catch (error) {
        showResult('sort-result', 'Error de conexión: ' + error.message, true);
    }
}

// Mostrar resultado
function showResult(containerId, message, isError = false) {
    const container = document.getElementById(containerId);
    const className = isError ? 'result error' : 'result';
    container.innerHTML = `<div class="${className}"><h3>${isError ? 'Error' : 'Resultado'}</h3><p>${message}</p></div>`;
}

// Eventos de teclado para mejorar UX
document.addEventListener('DOMContentLoaded', function () {
    // Enter para calcular
    document.getElementById('fraction1').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') calculate();
    });
    document.getElementById('fraction2').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') calculate();
    });

    // Enter para agregar fracciones
    document.getElementById('compare-fraction').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') addFraction('compare');
    });
    document.getElementById('sort-fraction').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') addFraction('sort');
    });
});