import React, { useEffect, useState } from "react";
import Head from "next/head"

function index(){
  const [message, setMessage] = useState("Loading");
  const [boardSize, setBoardSize] = useState({
    width:0,height:0
  });
  const [boardData, setBoardData] = useState([]);
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
              setBoardSize(()=>{
                return {
                  width:data.board_size.width,
                  height:data.board_size.height};
              })
              setBoardData([...data.coins]);
            })
          }}>
            Start
          </button>
          <button onClick={()=>{
            fetch("http://localhost:8080/api/next")
            .then((response) => response.json())
            .then((data) => {
              setBoardData([...data.coins]);
            })
          }}>
            Next 
          </button>
          <h1>{boardSize.width}x{boardSize.height}</h1>
        </div>
        <div className="board">
          {[...Array(8)].map((v,idy) => {
            return <div 
              key={idy} 
              className="row">
              {[...Array(8)].map((v,idx) => {
                return <div 
                  key={idx} 
                  className="square">
                  {
                    boardData
                    .filter((p) => {return (p.X === idx && p.Y === idy);})
                    .map((p) => {
                      if(p.Player === 'A'){
                        return (<div key={`{p.X}{p.Y}`} className="allyCoin"><h1 className="allyCoinText">{p.Coin}</h1></div>)
                      }else if(p.Player === 'B'){
                        return (<div key={`{p.X}{p.Y}`} className="enemyCoin"><h1 className="enemyCoinText">{p.Coin}</h1></div>)
                      }
                    })
                  }
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
