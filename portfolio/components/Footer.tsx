import React from 'react'

const Footer = () => {
  return (
    <footer className='w-full pt-20 pb-10' id='contact'>
      <div className='w-full absolute left-0 -bottom-72 min-h-96'>
        <img 
          src='footer-grid.svg'
          alt='grid'
          className='w-full h-full opacity-50'
        />
      </div>

      <div className='flex flex-col items-center'>
        <h1>
          Ready to take <span className='text-purple'>your</span> digital prescence to the next level
        </h1>
      </div>
    </footer>
  )
}

export default Footer
