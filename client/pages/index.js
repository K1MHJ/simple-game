import React, { useEffect, useState } from "react";
import Head from "next/head"

function index(){
  const [message, setMessage] = useState("Loading");

  useEffect(()=>{
    fetch("http://localhost:8080/api/home")
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message);
      });
  }, []);

  const [boardData, setBoardData] = useState({
    0:"",
    1:"",
    2:"",
    3:"",
    4:"",
    5:"",
    6:"",
    7:"",
    8:"",
  });

  return (
    <div>
      <Head>
        <title>Tic Tac Toe</title>
      </Head>
      <h1>Tic Tac Toe</h1>
      <div className="game">
        <div className="game_menu">
          <button>Next</button>
        </div>
        <div className="board">
          {[...Array(8)].map((v,idx) => {
            return <div 
              key={idx} 
              className="row">

              {[...Array(8)].map((v,idx) => {
                return <div 
                  key={idx} 
                  className="square">
                </div>;
              })}

            </div>;
          })}
        </div>
      </div>
    </div>
  );
}

export default index;
