import * as React from "react";

function CardBack() {
  return (
    <>
      <div className="div-back">
        <div className="div-2">
          <div className="div-3">
            <div className="div-4">
              <div className="div-5"></div>
              <div className="div-6-back"></div>
            </div>
          </div>
        </div>
      </div>{" "}
      <style jsx>{`
        .div-back {
          border-radius: 20px;
          border-color: rgba(255, 255, 255, 1);
          border-style: solid;
          border-width: 1px;
          background-color: black;
          position: relative;
          display: flex;
          flex-direction: column;
          justify-content: center;
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
          min-height: 100px; /* Example minimum height */
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
          min-height: 150px; /* Example minimum height */
        }

        .div-4 {
          justify-content: space-between;
          display: flex;
          flex-direction: column;
          padding: 8px 16px;
          min-height: 200px; /* Example minimum height */
        }
        .div-5 {
          font: 700 20px GT Pressura Trial, -apple-system, Roboto, Helvetica, sans-serif;
          color: white; /* Added white font color */
          min-height: 50px; /* Example minimum height */
        }
        .div-6-back {
          margin-top: 63px;
          font: 400 12px GT Sectra Display Trial, -apple-system, Roboto, Helvetica, sans-serif;
          color: white; /* Added white font color */
          min-height: 100px; /* Example minimum height */
        }
      `}</style>{" "}
    </>
  );
}

export default CardBack;
