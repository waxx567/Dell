import { gridItems } from "@/data";
import { BentoGrid, BentoGridItem } from "./ui/BentoGrid";

const Grid = () => {
  return (
    <section id="about">
      <BentoGrid className="w-full py-20">
        {gridItems.map(({ id, title, description, className, img, imgClassName, titleClassName, spareImg }) => (
          <BentoGridItem
            id={id}
            key={id}
            title={title}
            description={description}
            // remove icon prop
            // remove original classname condition
            className={className}
            // img={item.img}
            // imgClassName={item.imgClassName}
            // titleClassName={item.titleClassName}
            // spareImg={item.spareImg}
          />
        ))}
      </BentoGrid>
    </section>
  );
};

export default Grid;