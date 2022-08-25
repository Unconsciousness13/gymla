import React from "react";

export default function Footer() {
  return (
    <footer className="site-footer">
      <div className="container">
        <div className="row">
          <div className="col-md-8 col-sm-6 col-xs-12">
            <p className="copyright-text">
              Copyright &copy; 2022 All Rights Reserved by
              <a
                className="pako-copyright"
                href="https://www.pako.es/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Pako™
              </a>
            </p>
          </div>

          <div className="col-md-4 col-sm-6 col-xs-12">
            <ul className="social-icons">
              <li>
                <a
                  className="facebook"
                  href="https://www.facebook.com/Isabella.Plamenov/"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <i className="fa fa-facebook"></i>
                </a>
              </li>
              <li>
                <a
                  className="instagram"
                  href="https://www.instagram.com/isabellaplamenov/"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <i className="fa fa-instagram"></i>
                </a>
              </li>
              <li>
                <a
                  className="linkedin"
                  href="https://www.linkedin.com/in/plamen-iliev-b35646201/"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <i className="fa fa-linkedin"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
}
