import React from "react";
import STLViewer from "./components/stl";
// import {StlViewer} from "react-stl-viewer";
const style = {
    top: 0,
    left: 0,
    width: '100vw',
    height: '100vh',
}
function App() {
  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <STLViewer modelUrl="box.stl" />
      hi
      {/* <StlViewer
            style={style}
            orbitControls
            shadows
            url={"hollow_cone.stl"}
        /> */}
        bye
    </div>
  );
}

export default App;