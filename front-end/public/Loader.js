import React from 'https://esm.sh/react?dev';
import { RingLoader } from 'https://esm.sh/react-spinners';

const Loader = () => {
  return (
    <div className="loader">
      <RingLoader color={'#ccc'} size={80} />
    </div>
  );
};

export default Loader;
