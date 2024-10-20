export const navItems = [
  { name: "About", link: "#about" },
  { name: "Projects", link: "#projects" },
  { name: "Knowledge", link: "#testimonials" },
  { name: "Contact", link: "#contact" },
];

export const gridItems = [
  {
    id: 1,
    title: "I prioritize collaboration, fostering open communication ",
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
    iconLists: ["/harvard.svg", "/zoom.svg", "/bootstrap.svg", "/php.svg", "/github-grey.svg", "/sqlite.svg"],
    link: "/ui.earth.com",
  },
  {
    id: 2,
    title: "Python, HTML, CSS, and JavaScript projects",
    des: "Putting what I learned into practice with exercises, apps, and projects that interest me.",
    img: "/projects.jpg",
    iconLists: ["/python.svg", "/html.svg", "/css.svg", "/javascript.svg", "/re.svg", "/tail.svg", "/wordpress.svg"],
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
    name: "CS50AI Certificate 2024",
    title: "Harvard University",
  },
  {
    quote:
      "Salesforce is cloud-based CRM software, which makes it easier for companies to find more prospects, close more deals, and connect with customers in a whole new way, so they can provide them with amazing service at scale. I have acquired 82 badges, 55000+ points, 12 trails, and attained Expeditioner rank. I'm currently working on the Apex Specialist Superbadge, and plan to take the Platform App Builder & Platform Developer I certifications soonest.",
    name: "Salesforce 2024",
    title: "Trailhead Online Training",
  },
  {
    quote:
      "React is a front-end JavaScript library for building user interfaces based on components. Next.js for handling the user interface, Three.js for rendering 3D elements, Framer motion for beautiful animations, and styled with TailwindCSS. AceternityUI allowed developers to incorporate the most trending components. Sentry is an application monitoring platform that empowers developers to fix application problems without compromising on velocity. A key advantage of React is that it only rerenders those parts of the page that have changed, avoiding unnecessary re-rendering of unchanged DOM elements.",
    name: "React.js 2023 & 2024",
    title: "Traversy Media & JSMastery",
  },
  {
    quote:
      "Flask is a micro web framework written in Python that supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Flask uses Jinja templating, supports unit testing, and is compatible with Google App Engine. Applications that use the Flask framework include Pinterest and LinkedIn.",
    name: "Flask Web Framework2023",
    title: "Harvard University",
  },
  {
    quote:
      "GitHub is a developer platform that allows developers to create, store, manage and share their code. It uses Git software, providing the distributed version control of access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project. It is commonly used to host open source software development projects. GitHub is the world's largest source code host. It is commonly used to host open source software development projects.",
    name: "GitHub 2023",
    title: "Harvard University",
  },
  {
    quote:
      "WordPress is a web content management system. It was originally created as a tool to publish blogs but has evolved to support publishing other web content, including more traditional websites, mailing lists and Internet forum, media galleries, membership sites, learning management systems, and online stores. WordPress is  the most popular content management system in the world, and was used by 43.1% of the top 10 million websites in 2023.",
    name: "WordPress 2024",
    title: "wordpress.org",
  },
  {
    quote:
      "Bootstrap is an HTML, CSS and JS library that focuses on simplifying the development of informative web pages (as opposed to web applications). The primary purpose of adding it to a web project is to apply Bootstrap's choices of color, size, font and layout to that project. As such, the primary factor is whether the developers in charge find those choices to their liking. Bootstrap also comes with several JavaScript components which do not require other libraries like jQuery.",
    name: "Bootstrap 2023",
    title: "Harvard University",
  },
  {
    quote:
      "Frontend Mentor offers a variety of coding challenges for front-end developers of different levels. I improved my front-end skills by building real projects, and solved real-world HTML, CSS and JavaScript challenges whilst working to professional designs. I built projects, learn new skills, and joined the Discord community. This was an invaluable resource for me at a time when I was just starting out and unsure of my abilities.",
    name: "HTML, CSS & JavaScript 2023",
    title: "frontendmentor.io",
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
    title: "Dedicated and Enthusiastic",
    desc: "Committed to delivering high-quality code with a positive attitude and a passion for problem-solving.",
    className: "md:col-span-2",
    thumbnail: "/exp1.svg",
  },
  {
    id: 2,
    title: "Passionate and Conscientious",
    desc: "Driven by a love for coding, I pay attention to detail and strive for excellence in my work.",
    className: "md:col-span-2", // change to md:col-span-2
    thumbnail: "/exp2.svg",
  },
  {
    id: 3,
    title: "Eager to Learn and Contribute",
    desc: "Constantly learning new technologies and eager to apply them in real-world projects to add value.",
    className: "md:col-span-2", // change to md:col-span-2
    thumbnail: "/exp3.svg",
  },
  {
    id: 4,
    title: "Able to Work Independently",
    desc: "Capable of managing tasks effectively and delivering solutions while taking initiative and responsibility.",
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