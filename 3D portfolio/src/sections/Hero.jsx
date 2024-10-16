import { Suspense } from "react";
import { Canvas } from "@react-three/fiber";
import { PerspectiveCamera } from "@react-three/drei";
import CanvasLoader from "../components/CanvasLoader.jsx";
import { HackerRoom } from "../components/HackerRoom.jsx";

const Hero = () => {
  return (
    <section className="min-h-screen w-full flex flex-col relative">
        <div className="w-full mx-auto flex flex-col sm:mt-36 mt-20 c-space gap-3">
            <p className="sm:text-3xl text-2xl font-medium text-white text-center font-generalsans">Hi, I'm Wayne <span className="waving-hand">👋</span></p>
            <p className="hero_tag text-gray_gradient">Building Products & Brands</p>
        </div>

        <div className="w-full h-full absolute inset-0">
            <Canvas className="w-full h-full">
                <Suspense fallback={<CanvasLoader />}>
                    <PerspectiveCamera makeDefault position={[0, 0, 30]}/>

                    <HackerRoom scale={0.5} position={[0, 0, 0]} rotation={[0, -Math.PI / 2, 0]} />

                    <ambientLight intensity={1} />    
                </Suspense>
            </Canvas>
        </div>
    </section>
  )
}

export default Hero
