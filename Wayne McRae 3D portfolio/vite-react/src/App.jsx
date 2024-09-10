import {Canvas} from "@react-three/fiber";
import {OrbitControls} from "@react-three/drei";

const RotatingCube = () => {
  const meshRef = useRef()

  return (
    <mesh ref={meshRef}>

    </mesh>
  )
}

const App = () => {
  return (
    <Canvas style={{ height: '100vh', width: '100vw', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
      <OrbitControls enableZoom={true} enablePan enableRotate />

      <directionalLight position={[1, 1, 1]} intensity={10} color={0x9CDBA6} />

      <color attach="background" args={['#F0F0F0']} />

      <RotatingCube />
    </Canvas>
  )
}

export default App;