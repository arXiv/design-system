// Multi-select combobox with 4 independent sections. Complete arXiv categories from rOpenSci arxiv_cats reference.

const categories = [
  // Computer Science (40)
  { id: 'cs.AI', name: 'Artificial Intelligence' },
  { id: 'cs.AR', name: 'Hardware Architecture' },
  { id: 'cs.CC', name: 'Computational Complexity' },
  { id: 'cs.CE', name: 'Computational Engineering, Finance, and Science' },
  { id: 'cs.CG', name: 'Computational Geometry' },
  { id: 'cs.CL', name: 'Computation and Language' },
  { id: 'cs.CR', name: 'Cryptography and Security' },
  { id: 'cs.CV', name: 'Computer Vision and Pattern Recognition' },
  { id: 'cs.CY', name: 'Computers and Society' },
  { id: 'cs.DB', name: 'Databases' },
  { id: 'cs.DC', name: 'Distributed, Parallel, and Cluster Computing' },
  { id: 'cs.DL', name: 'Digital Libraries' },
  { id: 'cs.DM', name: 'Discrete Mathematics' },
  { id: 'cs.DS', name: 'Data Structures and Algorithms' },
  { id: 'cs.ET', name: 'Emerging Technologies' },
  { id: 'cs.FL', name: 'Formal Languages and Automata Theory' },
  { id: 'cs.GL', name: 'General Literature' },
  { id: 'cs.GR', name: 'Graphics' },
  { id: 'cs.GT', name: 'Computer Science and Game Theory' },
  { id: 'cs.HC', name: 'Human-Computer Interaction' },
  { id: 'cs.IR', name: 'Information Retrieval' },
  { id: 'cs.IT', name: 'Information Theory' },
  { id: 'cs.LG', name: 'Machine Learning' },
  { id: 'cs.LO', name: 'Logic in Computer Science' },
  { id: 'cs.MA', name: 'Multiagent Systems' },
  { id: 'cs.MM', name: 'Multimedia' },
  { id: 'cs.MS', name: 'Mathematical Software' },
  { id: 'cs.NA', name: 'Numerical Analysis' },
  { id: 'cs.NE', name: 'Neural and Evolutionary Computing' },
  { id: 'cs.NI', name: 'Networking and Internet Architecture' },
  { id: 'cs.OH', name: 'Other Computer Science' },
  { id: 'cs.OS', name: 'Operating Systems' },
  { id: 'cs.PF', name: 'Performance' },
  { id: 'cs.PL', name: 'Programming Languages' },
  { id: 'cs.RO', name: 'Robotics' },
  { id: 'cs.SC', name: 'Symbolic Computation' },
  { id: 'cs.SD', name: 'Sound' },
  { id: 'cs.SE', name: 'Software Engineering' },
  { id: 'cs.SI', name: 'Social and Information Networks' },
  { id: 'cs.SY', name: 'Systems and Control' },

  // Economics (3)
  { id: 'econ.EM', name: 'Econometrics' },
  { id: 'econ.GN', name: 'General Economics' },
  { id: 'econ.TH', name: 'Theoretical Economics' },

  // Electrical Engineering and Systems Science (4)
  { id: 'eess.AS', name: 'Audio and Speech Processing' },
  { id: 'eess.IV', name: 'Image and Video Processing' },
  { id: 'eess.SP', name: 'Signal Processing' },
  { id: 'eess.SY', name: 'Systems and Control' },

  // Mathematics (33)
  { id: 'math.AC', name: 'Commutative Algebra' },
  { id: 'math.AG', name: 'Algebraic Geometry' },
  { id: 'math.AP', name: 'Analysis of PDEs' },
  { id: 'math.AT', name: 'Algebraic Topology' },
  { id: 'math.CA', name: 'Classical Analysis and ODEs' },
  { id: 'math.CO', name: 'Combinatorics' },
  { id: 'math.CT', name: 'Category Theory' },
  { id: 'math.CV', name: 'Complex Variables' },
  { id: 'math.DG', name: 'Differential Geometry' },
  { id: 'math.DS', name: 'Dynamical Systems' },
  { id: 'math.FA', name: 'Functional Analysis' },
  { id: 'math.GM', name: 'General Mathematics' },
  { id: 'math.GN', name: 'General Topology' },
  { id: 'math.GR', name: 'Group Theory' },
  { id: 'math.GT', name: 'Geometric Topology' },
  { id: 'math.HO', name: 'History and Overview' },
  { id: 'math.IT', name: 'Information Theory' },
  { id: 'math.KT', name: 'K-Theory and Homology' },
  { id: 'math.LO', name: 'Logic' },
  { id: 'math.MG', name: 'Metric Geometry' },
  { id: 'math.MP', name: 'Mathematical Physics' },
  { id: 'math.NA', name: 'Numerical Analysis' },
  { id: 'math.NT', name: 'Number Theory' },
  { id: 'math.OA', name: 'Operator Algebras' },
  { id: 'math.OC', name: 'Optimization and Control' },
  { id: 'math.PR', name: 'Probability' },
  { id: 'math.QA', name: 'Quantum Algebra' },
  { id: 'math.RA', name: 'Rings and Algebras' },
  { id: 'math.RT', name: 'Representation Theory' },
  { id: 'math.SG', name: 'Symplectic Geometry' },
  { id: 'math.SP', name: 'Spectral Theory' },
  { id: 'math.ST', name: 'Statistics Theory' },

  // Physics: Astrophysics (6)
  { id: 'astro-ph.CO', name: 'Cosmology and Nongalactic Astrophysics' },
  { id: 'astro-ph.EP', name: 'Earth and Planetary Astrophysics' },
  { id: 'astro-ph.GA', name: 'Astrophysics of Galaxies' },
  { id: 'astro-ph.HE', name: 'High Energy Astrophysical Phenomena' },
  { id: 'astro-ph.IM', name: 'Instrumentation and Methods for Astrophysics' },
  { id: 'astro-ph.SR', name: 'Solar and Stellar Astrophysics' },

  // Physics: Condensed Matter (9)
  { id: 'cond-mat.dis-nn', name: 'Disordered Systems and Neural Networks' },
  { id: 'cond-mat.mes-hall', name: 'Mesoscale and Nanoscale Physics' },
  { id: 'cond-mat.mtrl-sci', name: 'Materials Science' },
  { id: 'cond-mat.other', name: 'Other Condensed Matter' },
  { id: 'cond-mat.quant-gas', name: 'Quantum Gases' },
  { id: 'cond-mat.soft', name: 'Soft Condensed Matter' },
  { id: 'cond-mat.stat-mech', name: 'Statistical Mechanics' },
  { id: 'cond-mat.str-el', name: 'Strongly Correlated Electrons' },
  { id: 'cond-mat.supr-con', name: 'Superconductivity' },

  // Physics: General Relativity & High Energy (14)
  { id: 'gr-qc', name: 'General Relativity and Quantum Cosmology' },
  { id: 'hep-ex', name: 'High Energy Physics - Experiment' },
  { id: 'hep-lat', name: 'High Energy Physics - Lattice' },
  { id: 'hep-ph', name: 'High Energy Physics - Phenomenology' },
  { id: 'hep-th', name: 'High Energy Physics - Theory' },
  { id: 'math-ph', name: 'Mathematical Physics' },
  { id: 'nlin.AO', name: 'Adaptation and Self-Organizing Systems' },
  { id: 'nlin.CD', name: 'Chaotic Dynamics' },
  { id: 'nlin.CG', name: 'Cellular Automata and Lattice Gases' },
  { id: 'nlin.PS', name: 'Pattern Formation and Solitons' },
  { id: 'nlin.SI', name: 'Exactly Solvable and Integrable Systems' },
  { id: 'nucl-ex', name: 'Nuclear Experiment' },
  { id: 'nucl-th', name: 'Nuclear Theory' },
  { id: 'quant-ph', name: 'Quantum Physics' },

  // Physics: General Categories (23)
  { id: 'physics.acc-ph', name: 'Accelerator Physics' },
  { id: 'physics.ao-ph', name: 'Atmospheric and Oceanic Physics' },
  { id: 'physics.app-ph', name: 'Applied Physics' },
  { id: 'physics.atm-clus', name: 'Atomic and Molecular Clusters' },
  { id: 'physics.atom-ph', name: 'Atomic Physics' },
  { id: 'physics.bio-ph', name: 'Biological Physics' },
  { id: 'physics.chem-ph', name: 'Chemical Physics' },
  { id: 'physics.class-ph', name: 'Classical Physics' },
  { id: 'physics.comp-ph', name: 'Computational Physics' },
  { id: 'physics.data-an', name: 'Data Analysis, Statistics and Probability' },
  { id: 'physics.ed-ph', name: 'Physics Education' },
  { id: 'physics.flu-dyn', name: 'Fluid Dynamics' },
  { id: 'physics.gen-ph', name: 'General Physics' },
  { id: 'physics.geo-ph', name: 'Geophysics' },
  { id: 'physics.hist-ph', name: 'History and Philosophy of Physics' },
  { id: 'physics.ins-det', name: 'Instrumentation and Detectors' },
  { id: 'physics.med-ph', name: 'Medical Physics' },
  { id: 'physics.optics', name: 'Optics' },
  { id: 'physics.plasm-ph', name: 'Plasma Physics' },
  { id: 'physics.pop-ph', name: 'Popular Physics' },
  { id: 'physics.soc-ph', name: 'Physics and Society' },
  { id: 'physics.space-ph', name: 'Space Physics' },

  // Quantitative Biology (10)
  { id: 'q-bio.BM', name: 'Biomolecules' },
  { id: 'q-bio.CB', name: 'Cell Behavior' },
  { id: 'q-bio.GN', name: 'Genomics' },
  { id: 'q-bio.MN', name: 'Molecular Networks' },
  { id: 'q-bio.NC', name: 'Neurons and Cognition' },
  { id: 'q-bio.OT', name: 'Other Quantitative Biology' },
  { id: 'q-bio.PE', name: 'Populations and Evolution' },
  { id: 'q-bio.QM', name: 'Quantitative Methods' },
  { id: 'q-bio.SC', name: 'Subcellular Processes' },
  { id: 'q-bio.TO', name: 'Tissues and Organs' },

  // Quantitative Finance (9)
  { id: 'q-fin.CP', name: 'Computational Finance' },
  { id: 'q-fin.EC', name: 'Economics' },
  { id: 'q-fin.GN', name: 'General Finance' },
  { id: 'q-fin.MF', name: 'Mathematical Finance' },
  { id: 'q-fin.PM', name: 'Portfolio Management' },
  { id: 'q-fin.PR', name: 'Pricing of Securities' },
  { id: 'q-fin.RM', name: 'Risk Management' },
  { id: 'q-fin.ST', name: 'Statistical Finance' },
  { id: 'q-fin.TR', name: 'Trading and Market Microstructure' },

  // Statistics (6)
  { id: 'stat.AP', name: 'Applications' },
  { id: 'stat.CO', name: 'Computation' },
  { id: 'stat.ME', name: 'Methodology' },
  { id: 'stat.ML', name: 'Machine Learning' },
  { id: 'stat.OT', name: 'Other Statistics' },
  { id: 'stat.TH', name: 'Statistics Theory' },
];

// Configuration for each section
const sections = {
  1: {
    selected: [
      categories.find(c => c.id === 'cs.AI'),
      categories.find(c => c.id === 'math.CO'),
      categories.find(c => c.id === 'physics.optics'),
    ],
    initialSelected: [],
    filtered: [],
    highlighted: -1,
  },
  2: {
    selected: [
      categories.find(c => c.id === 'cs.LG'),
      categories.find(c => c.id === 'stat.ML'),
    ],
    initialSelected: [],
    filtered: [],
    highlighted: -1,
  },
  3: {
    selected: [
      categories.find(c => c.id === 'cs.CV'),
      categories.find(c => c.id === 'physics.bio-ph'),
    ],
    initialSelected: [],
    filtered: [],
    highlighted: -1,
  },
  4: {
    selected: [
      categories.find(c => c.id === 'math.AP'),
    ],
    initialSelected: [],
    filtered: [],
    highlighted: -1,
  },
};

// --- Helper functions ---
function getInput(sectionNum) {
  return document.getElementById(`combo-input-${sectionNum}`);
}

function getListEl(sectionNum) {
  return document.getElementById(`combo-list-${sectionNum}`);
}

function getChipContainer(sectionNum) {
  return document.getElementById(`chip-container-${sectionNum}`);
}

function getModal(sectionNum) {
  return document.getElementById(`modal-${sectionNum}`);
}

function getModalChipDisplay(sectionNum) {
  return document.getElementById(`modal-chip-display-${sectionNum}`);
}

function filter(q, sectionNum) {
  const s = q.trim().toLowerCase();
  if (!s) { 
    sections[sectionNum].filtered = categories.slice(); 
    return; 
  }
  sections[sectionNum].filtered = categories.filter(it => (it.id + ' ' + it.name).toLowerCase().includes(s));
}

function renderList(sectionNum) {
  const listEl = getListEl(sectionNum);
  listEl.innerHTML = '';
  sections[sectionNum].filtered.forEach((it, idx) => {
    const li = document.createElement('li');
    li.textContent = `${it.id} — ${it.name}`;
    li.setAttribute('role', 'option');
    li.dataset.index = idx;
    li.tabIndex = -1;
    li.onclick = () => selectFromList(sectionNum, idx);
    li.addEventListener('mousemove', () => { 
      sections[sectionNum].highlighted = idx; 
      updateHighlight(sectionNum); 
    });
    listEl.appendChild(li);
  });
  updateHighlight(sectionNum);
}

function updateHighlight(sectionNum) {
  const listEl = getListEl(sectionNum);
  const nodes = Array.from(listEl.children);
  nodes.forEach((n, i) => {
    n.setAttribute('aria-selected', i === sections[sectionNum].highlighted ? 'true' : 'false');
  });
}

function selectFromList(sectionNum, idx) {
  const item = sections[sectionNum].filtered[idx];
  if (!item) return;
  if (!sections[sectionNum].selected.find(s => s.id === item.id)) {
    sections[sectionNum].selected.push(item);
  }
  const input = getInput(sectionNum);
  input.value = '';
  filter('', sectionNum);
  sections[sectionNum].highlighted = -1;
  renderList(sectionNum);
  if (!getModal(sectionNum).hasAttribute('hidden')) {
    updateModalDisplay(sectionNum);
  }
  input.focus();
}

// Endorsement source data for "Is Endorsed For" chips (section 3).
// type 'auto'  — set automatically by the system; no human endorser.
// type 'user'  — granted by a named admin; username links to their account page.
const endorsementSources = {
  'cs.CV':          { type: 'auto' },
  'physics.bio-ph': { type: 'user', username: 'bsmith' },
};

function renderChips(sectionNum) {
  const chipContainer = getChipContainer(sectionNum);
  chipContainer.innerHTML = '';
  const selected = sections[sectionNum].selected;
  if (selected.length === 0) {
    chipContainer.innerHTML = '<span style="color:#b0aba6;font-size:13px;">None</span>';
    return;
  }
  selected.forEach(it => {
    const chip = document.createElement('div');
    chip.className = 'chip';
    chip.textContent = it.id;

    // Section 3 only: annotate each chip with its endorsement source
    if (sectionNum === 3) {
      const src = endorsementSources[it.id];
      const badge = document.createElement('span');
      if (!src || src.type === 'auto') {
        badge.className = 'chip-source chip-source-auto';
        badge.textContent = 'auto';
      } else {
        badge.className = 'chip-source';
        const link = document.createElement('a');
        link.href = '#'; // would be: /admin/user/${src.username}
        link.textContent = src.username;
        link.title = `Endorsed by ${src.username}`;
        badge.appendChild(link);
      }
      chip.appendChild(badge);
    }

    chipContainer.appendChild(chip);
  });
}

function updateModalDisplay(sectionNum) {
  const modalChipDisplay = getModalChipDisplay(sectionNum);
  const selected = sections[sectionNum].selected;
  modalChipDisplay.innerHTML = '';
  
  if (selected.length === 0) {
    modalChipDisplay.innerHTML = '<span style="color:#6b7280;">No categories selected</span>';
  } else {
    selected.forEach((it) => {
      const chip = document.createElement('div');
      chip.className = 'chip';
      chip.textContent = it.id;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.innerHTML = '✕';
      btn.title = 'Remove';
      btn.style.marginLeft = '8px';
      btn.style.background = 'transparent';
      btn.style.border = '0';
      btn.style.cursor = 'pointer';
      btn.style.color = '#334155';
      btn.style.padding = '0';
      btn.onclick = (e) => {
        e.stopPropagation();
        const idx = selected.findIndex(s => s.id === it.id);
        if (idx >= 0) selected.splice(idx, 1);
        updateModalDisplay(sectionNum);
      };
      chip.appendChild(btn);
      modalChipDisplay.appendChild(chip);
    });
  }
}

function openModal(sectionNum) {
  sections[sectionNum].initialSelected = sections[sectionNum].selected.map(s => ({...s}));
  
  updateModalDisplay(sectionNum);
  
  const modal = getModal(sectionNum);
  modal.removeAttribute('hidden');
}

function closeModal(sectionNum) {
  sections[sectionNum].selected = sections[sectionNum].initialSelected.map(s => ({...s}));
  renderChips(sectionNum);
  
  const modal = getModal(sectionNum);
  modal.setAttribute('hidden', '');
  const input = getInput(sectionNum);
  input.value = '';
  filter('', sectionNum);
  renderList(sectionNum);
}

function saveChanges(sectionNum) {
  renderChips(sectionNum);
  const modal = getModal(sectionNum);
  modal.setAttribute('hidden', '');
  const input = getInput(sectionNum);
  input.value = '';
  filter('', sectionNum);
  renderList(sectionNum);
}

// --- Initialization ---

// Render chips for all four sections on page load
for (let sectionNum = 1; sectionNum <= 4; sectionNum++) {
  renderChips(sectionNum);
}

// Sections 1 (Moderates) and 3 (Is Endorsed For) are editable — set up modals + event listeners.
// Sections 2 (Can Submit To) and 4 (Can Endorse For) are lookup-only — chips only, no modal.
const editableSections = [1, 3];

for (const sectionNum of editableSections) {
  sections[sectionNum].filtered = categories.slice();
  renderList(sectionNum);

  const editBtn      = document.getElementById(`editBtn-${sectionNum}`);
  const closeModalBtn = document.getElementById(`closeModal-${sectionNum}`);
  const cancelBtn    = document.getElementById(`cancelBtn-${sectionNum}`);
  const saveBtn      = document.getElementById(`saveBtn-${sectionNum}`);
  const modalOverlay = getModal(sectionNum).querySelector('.modal-overlay');
  const input        = getInput(sectionNum);
  const listEl       = getListEl(sectionNum);

  editBtn.addEventListener('click', () => openModal(sectionNum));
  closeModalBtn.addEventListener('click', () => closeModal(sectionNum));
  cancelBtn.addEventListener('click', () => closeModal(sectionNum));
  saveBtn.addEventListener('click', () => saveChanges(sectionNum));
  modalOverlay.addEventListener('click', () => closeModal(sectionNum));

  input.addEventListener('focus', () => {
    listEl.style.display = 'block';
    input.setAttribute('aria-expanded', 'true');
  });

  input.addEventListener('input', (e) => {
    filter(e.target.value, sectionNum);
    renderList(sectionNum);
    listEl.style.display = sections[sectionNum].filtered.length ? 'block' : 'none';
    input.setAttribute('aria-expanded', sections[sectionNum].filtered.length ? 'true' : 'false');
  });

  input.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (sections[sectionNum].highlighted < sections[sectionNum].filtered.length - 1)
        sections[sectionNum].highlighted++;
      updateHighlight(sectionNum);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (sections[sectionNum].highlighted > 0)
        sections[sectionNum].highlighted--;
      updateHighlight(sectionNum);
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (sections[sectionNum].highlighted >= 0)
        selectFromList(sectionNum, sections[sectionNum].highlighted);
    } else if (e.key === 'Backspace' && input.value === '') {
      if (sections[sectionNum].selected.length) {
        sections[sectionNum].selected.pop();
        renderChips(sectionNum);
        if (!getModal(sectionNum).hasAttribute('hidden')) {
          updateModalDisplay(sectionNum);
        }
      }
    }
  });

  document.addEventListener('click', (ev) => {
    const searchContainer = document.getElementById(`combobox-${sectionNum}`).querySelector('.search-container');
    if (!searchContainer.contains(ev.target)) {
      listEl.style.display = 'none';
      input.setAttribute('aria-expanded', 'false');
    }
  });
}
