import * as React from "react";

function CardFront({ responseText }) {
  // Receive responseText as a prop
  return (
    <>
      <div className="div-dark-img">
        <div className="div-2">
          <div className="div-3">
            <div className="div-4">
              {/* <div className='div-5'>Yann LeCun</div> */}
              <div className="div-6">
                {responseText} {/* Display the responseText */}
              </div>
            </div>
          </div>
        </div>
      </div>{" "}
      <style jsx>{`
        .div-dark-img {
          border-radius: 20px;
          border-color: rgba(255, 255, 255, 1);
          border-style: solid;
          border-width: 1px;
          background-color: rgba(24, 24, 24, 0.75);
          position: relative;
          display: flex;
          flex-direction: column;
          justify-content: center;
          background-image: url(https://cdn.builder.io/api/v1/image/assets%2Fd42d03f8f61140eabd49e1452ecee5be%2F8353d2745e604d6290e49423db828687);
          background-repeat: no-repeat;
          background-position: center;
          background-size: cover;
          padding: 21px 10px;
          width: 343px; /* Fixed width */
          height: 480px; /* Fixed height */
        }
        .div-2 {
          border-color: rgba(255, 255, 255, 1);
          border-style: solid;
          border-width: 1px;
          display: flex;
          flex-direction: column;
          justify-content: center;
          padding: 0 11px;
        }
        .div-3 {
          border-color: rgba(255, 255, 255, 1);
          border-style: solid;
          border-width: 1px;
          z-index: 10;
          display: flex;
          flex-direction: column;
          justify-content: center;
          margin: -11px 0 -10px;
          padding: 18px 3px;
        }

        .div-4 {
          justify-content: space-between;
          display: flex;
          flex-direction: column;
          padding: 8px 16px;
        }
        .div-5 {
          font: 700 20px GT Pressura Trial, -apple-system, Roboto, Helvetica, sans-serif;
          color: white; /* Added white font color */
        }
        .div-6 {
          font: 400 16px GT Sectra Display Trial, -apple-system, Roboto, Helvetica, sans-serif;
          color: white; /* Added white font color */
        }
      `}</style>{" "}
    </>
  );
}

export default CardFront;
