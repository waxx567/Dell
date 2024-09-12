# Wayne McRae 3D Portfolio

## Project overview

🤖 Introduction

This portfolio website was built with React.js for handling the user interface, Three.js for rendering 3D elements, and styled with TailwindCSS.
The primary goal is to demonstrate my skills in a unique manner and leave a lasting impact.

⚙️ Tech Stack

- Node.js
- React.js
- Three.js
- React Three Fiber
- React Three Drei
- Email JS
- Vite
- Tailwind CSS

🔋 Features

👉 Immersive Hero: An eye-catching 3D hacker room that responds to mouse movements, surrounded by animated mini-models.

👉 Interactive About Me: A sleek bento grid layout featuring personal info, a 3D globe pinpointing location, tech stack icons, and a one-click email copy option.

👉 Dynamic Project Showcase: Browse through projects while watching live demos inside a 3D computer model, seamlessly switching between different projects.

👉 Engaging Experience Timeline: Hover over career milestones to trigger interactive 3D animations that bring your professional journey to life.

👉 Client Testimonials: A dedicated section highlighting satisfied clients and their feedback.

👉 Easy Contact Form: A user-friendly email form for visitors to reach out directly from your portfolio.

👉 Clean Footer: A minimalist design featuring social media links for easy networking.

👉 Fully Responsive: Optimized layout ensuring a smooth experience across all devices, from desktop to mobile.

and many more, including code architecture and reusability

## React.js Overview

React is a free and open-source front-end JavaScript library for building user interfaces based on components by Facebook Inc. It is maintained by Meta (formerly Facebook) and a community of individual developers and companies.

React can be used to develop single-page, mobile, or server-rendered applications with frameworks like Next.js. Because React is only concerned with the user interface and rendering components to the DOM, React applications often rely on libraries for routing and other client-side functionality. A key advantage of React is that it only rerenders those parts of the page that have changed, avoiding unnecessary rerendering of unchanged DOM elements.

[Wikipedia Link](https://en.wikipedia.org/wiki/React_(JavaScript_library))

## Three.js Overview

Three.js is a lightweight and flexible JavaScript library designed to enable the creation of complex 3D visualizations, animations, and interactive graphics within a web browser. It abstracts many of the complexities associated with WebGL, making it easier for developers to render 3D objects, apply materials, and create immersive experiences with relatively minimal code.

## Key Features of Three.js

**Rendering Engine:** Three.js provides an efficient rendering engine that makes use of WebGL to render 3D graphics directly in the browser. It also supports alternative renderers, including CanvasRenderer and SVGRenderer, to ensure compatibility with older browsers that may not support WebGL.

**Scene Graph:** Three.js uses a scene graph structure, which organizes all objects (like cameras, lights, and 3D meshes) into a hierarchy. This system allows for easy manipulation of objects in the 3D scene and simplifies transformations, like scaling, rotating, and translating objects.

**Geometry and Materials:** The library includes various built-in geometry types such as BoxGeometry, SphereGeometry, and PlaneGeometry. These can be used to create basic 3D shapes. You can also apply different materials like MeshBasicMaterial, MeshLambertMaterial, and MeshStandardMaterial to define how the surface of a 3D object interacts with light.

**Cameras:** Three.js offers multiple camera types, including PerspectiveCamera and OrthographicCamera, giving developers control over how the scene is viewed. The PerspectiveCamera mimics how human eyes perceive depth, making it suitable for most 3D scenes.

**Lighting:** Various light types can be used to illuminate a 3D scene, such as AmbientLight, PointLight, SpotLight, and DirectionalLight. These can be used to create realistic lighting effects, including shadows, reflections, and specular highlights.

**Textures and Environment Maps:** Three.js supports the application of textures to objects, allowing for detailed surface visuals. It also supports environment mapping, which can be used for reflective surfaces like metal or glass.

**Animation System:** Three.js includes a robust animation system that allows for animating object properties, such as position, rotation, or material attributes. It also supports keyframe animations, making it easier to animate 3D models imported from external tools like Blender or 3ds Max.

**Advanced Features:** For more advanced users, Three.js provides functionality for handling shaders, post-processing effects, and physics-based rendering (PBR). These can be combined to achieve highly realistic visual effects.

## Common Use Cases for Three.js

**Interactive 3D Portfolios:** Three.js is ideal for showcasing 3D models or animations in online portfolios, providing a visually engaging way to present work in fields like 3D modeling, architecture, or design.

**Data Visualization:** It can be used to create 3D charts, graphs, and interactive data representations, allowing users to interact with data in three dimensions.

**Games and Simulations:** With its built-in support for physics and lighting, Three.js is commonly used in web-based games, simulations, and virtual reality (VR) experiences.

**Architectural Visualization:** Architects use Three.js to render interactive 3D models of buildings, allowing clients to explore spaces before they are built.

## Why Use Three.js for a 3D Portfolio Website?

For a 3D portfolio, Three.js is an excellent choice because it provides:

**Cross-Browser Compatibility:** The WebGL engine ensures that your 3D content runs efficiently across modern browsers on both desktop and mobile devices.

**Ease of Integration:** Three.js integrates seamlessly with HTML, CSS, and JavaScript, allowing you to blend your 3D elements with standard web development technologies.

**Customizable Interactivity:** With Three.js, you can create custom user interactions, such as clicking on objects, dragging, zooming, or rotating the 3D scene, offering a highly interactive experience.

**Optimized Performance:** Despite its powerful features, Three.js is optimized for performance, ensuring that your website remains responsive and efficient, even with complex 3D scenes.

Three.js provides a user-friendly and versatile framework for developing interactive 3D content in the browser. Its wide range of built-in features, combined with the flexibility to customize and extend functionality, makes it a valuable tool for creating visually impressive and engaging websites like a 3D portfolio.

### Acknowledgement

Adrian Hajdin - JavaScript Mastery
[Video](https://www.youtube.com/watch?v=kt0FrkQgw8w&list=PLs4GO2nEDaoc_OBIdmCcVJSV_rn0FiARD&index=1&t=2460s)
`50:20` npm create vite@latest
