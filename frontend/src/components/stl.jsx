import React, { Suspense, useRef, useEffect } from "react";
import { Canvas, useLoader } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader";
import { VertexNormalsHelper } from "three/examples/jsm/helpers/VertexNormalsHelper";
import * as THREE from "three";

const STLModel = ({ url }) => {
  const geometry = useLoader(STLLoader, url);
  const meshRef = useRef();

  useEffect(() => {
    if (meshRef.current) {
      const helper = new VertexNormalsHelper(meshRef.current, 2, 0xff0000);
      meshRef.current.add(helper);
    }
  }, []);

  return (
    <mesh ref={meshRef}>
      <primitive object={geometry} attach="geometry" />
      <meshStandardMaterial color="gray" transparent opacity={0.3} side={THREE.DoubleSide} />
    </mesh>
  );
};

const STLViewer = ({ modelUrl }) => {
  return (
    <Canvas camera={{ position: [0, 0, 5] }}>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      <Suspense fallback={null}>
        <STLModel url={modelUrl} />
      </Suspense>
      <OrbitControls />
    </Canvas>
  );
};

export default STLViewer;
