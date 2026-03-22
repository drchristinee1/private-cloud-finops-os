async function loadData() {
  const response = await fetch('sample-data.json');
  const data = await response.json();

  renderStats(data.summary);
  renderAllocation(data.team_allocation);
  renderRateCard(data.rate_card);
}

function renderStats(summary) {
  const stats = [
    { label: 'Total Monthly Cost', value: money(summary.total_monthly_cost) },
    { label: 'Total Budget', value: money(summary.total_budget) },
    { label: 'Allocated Teams', value: String(summary.teams_allocated) },
    { label: 'Budget Variance', value: signedMoney(summary.total_variance) }
  ];

  const container = document.getElementById('stats');
  container.innerHTML = '';

  stats.forEach(item => {
    const card = document.createElement('div');
    card.className = 'stat-card';
    card.innerHTML = `
      <div class="label">${item.label}</div>
      <div class="value">${item.value}</div>
    `;
    container.appendChild(card);
  });
}

function renderAllocation(rows) {
  const tbody = document.querySelector('#allocationTable tbody');
  tbody.innerHTML = '';

  rows.forEach(row => {
    const tr = document.createElement('tr');
    const varianceClass = row.variance >= 0 ? 'negative' : 'positive';

    tr.innerHTML = `
      <td>${row.team}</td>
      <td>${money(row.allocated_cost)}</td>
      <td>${money(row.budget)}</td>
      <td class="${varianceClass}">${signedMoney(row.variance)}</td>
    `;
    tbody.appendChild(tr);
  });
}

function renderRateCard(rows) {
  const tbody = document.querySelector('#rateCardTable tbody');
  tbody.innerHTML = '';

  rows.forEach(row => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${row.unit}</td>
      <td>${row.rate}</td>
    `;
    tbody.appendChild(tr);
  });
}

function money(value) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0
  }).format(value);
}

function signedMoney(value) {
  const formatted = money(Math.abs(value));
  return value > 0 ? `+${formatted}` : `-${formatted}`;
}

document.getElementById('reloadData').addEventListener('click', loadData);
loadData();
