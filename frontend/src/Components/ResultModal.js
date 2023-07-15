function ResultModal({ showModal, closeModal, result }) {
    if (!showModal) {
        return null;
    }
    
  return (
    <div className='modal-overlay' onClick={closeModal}>
      <div className='modal-content' onClick={(e) => e.stopPropagation()}>
        <h3>Result</h3>
        <p>{result}</p>
        <button onClick={closeModal}>Close</button>
      </div>
    </div>
  );
};

export default ResultModal;
