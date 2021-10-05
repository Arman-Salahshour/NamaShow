import Header from "../../components/Header";
import Navbar from "../../components/Navbar";
import EmblaCarousel from "../../components/EmblaCarousel";
import Link from "next/dist/client/link";
import Footer from "../../components/Footer";

const Animations = () => {

    const SLIDE_COUNT = 5;
    const slides = Array.from(Array(SLIDE_COUNT).keys());
    return ( <div className="animations-page">
         <Header />
        <div className="home-main">
            <div className="main-content">
            <EmblaCarousel slides={slides} />
            <div className="popular">
                <div className="popular-title">
                    <p>مشاهده بیش تر</p>
                    <h3>انیمیشن های محبوب</h3>
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
 
export default Animations;