import Header from "./Header";
import Navbar from "./Navbar";
import EmblaCarousel from "./EmblaCarousel";
import Link from "next/dist/client/link";
import Footer from "./Footer";
import share1 from "../public/Images/Frame 85.svg"
import share2 from "../public/Images/Frame 85 (1).svg"
import share3 from "../public/Images/Frame 86.svg"
import { useEffect } from 'react'

const HomePage = () => {

    useEffect(() => {
        var x = window.matchMedia("(max-width: 922px)")
        var value = localStorage.getItem("modal")
        if (x.matches && value == null) {
            console.log(value);
           document.getElementById("myModal").style.display = "block"
      
        }
              var modal = document.getElementById("myModal");
      
      
              
              var span = document.getElementsByClassName("close1")[0];
              
              if (modal != null) {
              
                
            
              
              
              span.onclick = function() {
                modal.style.display = "none";
                localStorage.setItem('modal',"close");
              }
              
              
              window.onclick = function(event) {
                if (event.target == modal) {
                  modal.style.display = "none";
                }
              }
          }
      
    },[])
    const SLIDE_COUNT = 5;
const slides = Array.from(Array(SLIDE_COUNT).keys());
    return ( <div className="home-page">
        <Header />
        <div id="myModal" className="modal">

<div className="modal-content">
  
  <div className="modal-main">


 <h3>وب اپلیکیشن سینما را به صفحه اصلی اضافه کنید و به راحتی از امکانات آن استفاده کنید </h3>
 <div className="share-info">
     <div className="si1"><p>در نوار پایین روی دکمه Share بزنید.</p><img src={share1.src} /></div>
     <div className="si1"><p> در ﻣﻨﻮی ﺑﺎز ﺷﺪه در ﻗﺴﻤﺖ ﭘﺎﯾﯿﻦ ﺻﻔﺤﻪ، ﮔﺰﯾﻨﻪ Add To Home Screen را انتخاب کنید.</p><img src={share2.src}/></div>
     <div className="si1"><p>در مرحله بعد در قسمت بالا روی Add بزنید. </p><img src={share3.src} /> </div>
 </div>
 <div className="mm-btn"><button className="close1">متوجه شدم</button>  </div>
 



</div>
</div>
</div>
        <div className="home-main">
            <div className="main-content">
            <EmblaCarousel slides={slides} />
            <div className="popular">
                <div className="popular-title">
                    <p>مشاهده بیش تر</p>
                    <h3>فیلم های محبوب</h3>
                </div>
                <div className="popular-items">
                <Link href="/movies/her"><a >  <div className="popular-item">
                        <img src="/Images/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_.jpg" alt="Popular Movie" id="pop-mov"/>
                        <h4>Her</h4>
                        <div className="rating">
                            <img src="/Images/star.svg" alt="" />
                            <p>7.8</p>
                        </div>
                    </div>
                    </a>  
                    </Link>
                    <Link href="/movies/her"><a >   <div className="popular-item">
                        <img src="/Images/Spider-Man-No-Way-Home-poster.jpg" alt="Popular Movie" id="pop-mov"/>
                        <h4>Spider Man : no way home</h4>
                        <div className="rating">
                            <img src="/Images/star.svg" alt="" />
                            <p>6.8</p>
                        </div>
                    </div>
                    </a>
                    </Link >
                    <Link href="/movies/her"><a >  <div className="popular-item">
                        <img src="/Images/Green-Book-2018.jpg" alt="Popular Movie" id="pop-mov"/>
                        <h4>Green Book</h4>
                        <div className="rating">
                            <img src="/Images/star.svg" alt="" />
                            <p>8.4</p>
                        </div>
                    </div>
                    </a>
                    </Link>
                    <Link href="/movies/her"><a > <div className="popular-item">
                        <img src="/Images/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_FMjpg_UX1000_.jpg" alt="Popular Movie" id="pop-mov"/>
                        <h4>Black Panther</h4>
                        <div className="rating">
                            <img src="/Images/star.svg" alt="" />
                            <p>6.5</p>
                        </div>
                    </div>
                    </a>
                    </Link>
                    <Link href="/movies/her"><a > <div className="popular-item">
                        <img src="/Images/99f8702093bd74454c4636a33f558c4a.png" alt="Popular Movie" id="pop-mov"/>
                        <h4>Joker</h4>
                        <div className="rating">
                            <img src="/Images/star.svg" alt="" />
                            <p>7.9</p>
                        </div>
                    </div>
                    </a>
                    </Link>
                    <Link href="/movies/her"><a > <div className="popular-item">
                        <img src="/Images/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_.jpg" alt="Popular Movie" id="pop-mov"/>
                        <h4>Her</h4>
                        <div className="rating">
                            <img src="/Images/star.svg" alt="" />
                            <p>6.8</p>
                        </div>
                    </div>
                    </a>
                    </Link>
                </div>
            </div>
            </div>
            <Navbar />
        </div>
        <Footer />
    </div> );
}
 
export default HomePage;