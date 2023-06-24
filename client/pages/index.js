import React, { useEffect, useState } from "react";
import Head from "next/head"

function index(){
  const [message, setMessage] = useState("Loading");

  // useEffect(()=>{
  //   fetch("http://localhost:8080/api/home")
  //     .then((response) => response.json())
  //     .then((data) => {
  //       setMessage(data.message);
  //     });
  // }, []);

  const [boardSize, setBoardSize] = useState({
    width:0,height:0
  });
  const [boardData, setBoardData] = useState(
    [{X:0,Y:0,Player:"",Coin:0}]
  );

  return (
    <div>
      <Head>
        <title>Tic Tac Toe</title>
      </Head>
      <h1>Tic Tac Toe</h1>
      <div className="game">
        <div className="game_menu">
          <button onClick={()=>{
            fetch("http://localhost:8080/api/start")
            .then((response) => response.json())
            .then((data) => {
              console.log(data.board_size),
              setBoardSize(()=>{
                return {
                width:data.board_size.width,
                height:data.board_size.height};
              })
            });
          }}>
            Start
          </button>
          <h1>{boardSize.width}x{boardSize.height}</h1>
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
