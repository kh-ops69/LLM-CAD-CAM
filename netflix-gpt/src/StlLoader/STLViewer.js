import React from "react";
import { Canvas, useLoader } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import * as THREE from "three";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";

const STLModel = ({ fileUrl }) => {
    console.log("Loading STL file from:", fileUrl);
    const geometry = useLoader(STLLoader, fileUrl);
    
    console.log("Loaded geometry:", geometry); // Debugging
  
    const material = new THREE.MeshStandardMaterial({ color: "white", wireframe: true });
  
    return (
      <mesh geometry={geometry} material={material} scale={0.5}>
        <pointLight position={[10, 10, 10]} />
      </mesh>
    );
  };
  

const STLViewer = ({ fileUrl }) => {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 50 }}>
      <ambientLight intensity={0.5} />
      <STLModel fileUrl={fileUrl} />
      <OrbitControls />
    </Canvas>
  );
};

export default STLViewer;
