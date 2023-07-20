function ResultModal({ showModal, closeModal, result }) {
    if (!showModal) {
        return null;
    }
    
  return (
    <div className='modal-overlay' onClick={closeModal}>
      <div className='modal-content' onClick={(e) => e.stopPropagation()}>
        <button className='close-button' onClick={closeModal}>X</button>
        <h3>Result</h3>
        <p>The chances of getting lung cancer is: {result}</p>
      </div>
    </div>
  );
};

export default ResultModal;
