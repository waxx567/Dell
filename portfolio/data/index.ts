export const navItems = [
  { name: "About", link: "#about" },
  { name: "Projects", link: "#projects" },
  { name: "Testimonials", link: "#testimonials" },
  { name: "Contact", link: "#contact" },
];

export const gridItems = [
  {
    id: 1,
    title: "I prioritize client collaboration, fostering open communication ",
    description: "",
    className: "lg:col-span-3 md:col-span-6 md:row-span-4 lg:min-h-[90vh]",
    imgClassName: "w-full h-full",
    titleClassName: "justify-end",
    img: "/b1.svg",
    spareImg: "",
  },
  {
    id: 2,
    title: "I'm very flexible with time zone communications",
    description: "",
    className: "lg:col-span-2 md:col-span-3 md:row-span-2",
    imgClassName: "",
    titleClassName: "justify-start",
    img: "",
    spareImg: "",
  },
  {
    id: 3,
    title: "My tech stack",
    description: "I constantly try to improve",
    className: "lg:col-span-2 md:col-span-3 md:row-span-2",
    imgClassName: "",
    titleClassName: "justify-center",
    img: "",
    spareImg: "",
  },
  {
    id: 4,
    title: "Tech enthusiast with a passion for development.",
    description: "",
    className: "lg:col-span-2 md:col-span-3 md:row-span-1",
    imgClassName: "",
    titleClassName: "justify-start",
    img: "/grid.svg",
    spareImg: "/b4.svg",
  },

  {
    id: 5,
    title: "Currently building a JS Animation library",
    description: "The Inside Scoop",
    className: "md:col-span-3 md:row-span-2",
    imgClassName: "absolute right-0 bottom-0 md:w-96 w-60",
    titleClassName: "justify-center md:justify-start lg:justify-center",
    img: "/b5.svg",
    spareImg: "/grid.svg",
  },
  {
    id: 6,
    title: "Do you want to start a project together?",
    description: "",
    className: "lg:col-span-2 md:col-span-3 md:row-span-1",
    imgClassName: "",
    titleClassName: "justify-center md:max-w-full max-w-60 text-center",
    img: "",
    spareImg: "",
  },
];

export const projects = [
  {
    id: 1,
    title: "CS50X 2023, CS50P 2023, CS50AI 2024",
    des: "CS50 is a computer science course taught at Harvard University, Yale University and Dartmouth College.",
    img: "/harvard.png",
    iconLists: ["/harvard.svg", "/bootstrap.svg", "/php.svg", "/sqlite.svg", "/zoom.svg"],
    link: "/ui.earth.com",
  },
  {
    id: 2,
    title: "Python, HTML, CSS, and JavaScript projects",
    des: "Putting what I learned into practice with exercises, apps, and projects that interest me.",
    img: "/projects.jpg",
    iconLists: ["/python.svg", "/html.svg", "/css.svg", "/javascript.svg", "/re.svg", "/tail.svg"],
    link: "/ui.yoom.com",
  },
  {
    id: 3,
    title: "Salesforce badges, trails, and rank attained",
    des: "Salesforce is the world's #1 CRM platform that connects all your data, teams, and AI on one integrated system.",
    img: "/salesforce.jpg",
    iconLists: ["/salesforce.svg", "/slack.svg"],
    link: "/ui.aiimg.com",
  },
  {
    id: 4,
    title: "My portfolio website",
    des: "Demonstrating my skills as a developer with 3D elements and a smooth UI experience. Optimized and deployed efficiently.",
    img: "/portfolio.jpg",
    iconLists: ["/next.svg", "/tail.svg", "/ts.svg", "/three.svg", "/sentry.svg", "/host.svg"],
    link: "#",
  },
];

export const testimonials = [
  {
    quote:
      "CS50X teaches students to solve problems, both with and without code, emphasizing correctness, design, and style. Topics generally include computational thinking, abstraction, algorithms, data structures, and computer science. I learned to program in C, Python, HTML, CSS, and JavaScript, design, query, and process SQL databases. I also gained an understanding of computer hardware, industry best practices, and memory allocation.",
    name: "CS50X Certificate 2023",
    title: "Harvard University",
  },
  {
    quote:
      "CS50P taught me how to read and write Python code, including testing and debugging. This course covers functions, arguments, return values, variables and types, conditionals, Boolean expressions, and loops. I learned how to handle exceptions, use third-party libraries, validate and extract data with regular expressions, model real-world entities with classes, objects, methods, and properties, and read and write files.",
    name: "CS50P Certificate 2023",
    title: "Harvard University",
  },
  {
    quote:
      "CS50AI explores the concepts and algorithms of modern artificial intelligence, diving into the ideas that give rise to technologies like game-playing engines, handwriting recognition, machine translation, graph search algorithms, classification, optimization, machine learning, large language models. Students emerge with experience in libraries for machine learning as well as knowledge of AI principles to design intelligent systems of their own.",
    name: "CS50AI Certificate 2023",
    title: "Harvard University",
  },
  {
    quote:
      "Collaborating with Wayne was an absolute pleasure. His professionalism, promptness, and dedication to delivering exceptional results were evident throughout our project. Wayne's enthusiasm for every facet of development truly stands out. If you're seeking to elevate your website and elevate your brand, Wayne is the ideal partner.",
    name: "Michael Johnson",
    title: "Director of AlphaStream Technologies",
  },
  {
    quote:
      "Collaborating with Wayne was an absolute pleasure. His professionalism, promptness, and dedication to delivering exceptional results were evident throughout our project. Wayne's enthusiasm for every facet of development truly stands out. If you're seeking to elevate your website and elevate your brand, Wayne is the ideal partner.",
    name: "Michael Johnson",
    title: "Director of AlphaStream Technologies",
  },
];

export const companies = [
  {
    id: 1,
    name: "cloudinary",
    img: "/cloud.svg",
    nameImg: "/cloudName.svg",
  },
  {
    id: 2,
    name: "appwrite",
    img: "/app.svg",
    nameImg: "/appName.svg",
  },
  {
    id: 3,
    name: "HOSTINGER",
    img: "/host.svg",
    nameImg: "/hostName.svg",
  },
  {
    id: 4,
    name: "stream",
    img: "/s.svg",
    nameImg: "/streamName.svg",
  },
  {
    id: 5,
    name: "docker.",
    img: "/dock.svg",
    nameImg: "/dockerName.svg",
  },
];

export const workExperience = [
  {
    id: 1,
    title: "Frontend Engineer Intern",
    desc: "Assisted in the development of a web-based platform using React.js, enhancing interactivity.",
    className: "md:col-span-2",
    thumbnail: "/exp1.svg",
  },
  {
    id: 2,
    title: "Mobile App Dev - JSM Tech",
    desc: "Designed and developed mobile app for both iOS & Android platforms using React Native.",
    className: "md:col-span-2", // change to md:col-span-2
    thumbnail: "/exp2.svg",
  },
  {
    id: 3,
    title: "Freelance App Dev Project",
    desc: "Led the dev of a mobile app for a client, from initial concept to deployment on app stores.",
    className: "md:col-span-2", // change to md:col-span-2
    thumbnail: "/exp3.svg",
  },
  {
    id: 4,
    title: "Lead Frontend Developer",
    desc: "Developed and maintained user-facing features using modern frontend technologies.",
    className: "md:col-span-2",
    thumbnail: "/exp4.svg",
  },
];

export const socialMedia = [
  {
    id: 1,
    img: "/git.svg",
  },
  {
    id: 2,
    img: "/twit.svg",
  },
  {
    id: 3,
    img: "/link.svg",
  },
];