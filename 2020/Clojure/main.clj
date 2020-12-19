(ns main
  (:require [clojure.java.io :as io]))

(defmulti part1 identity)
(defmulti part2 identity)

(defmacro defoverload
  "Register a method IMPL to MULTIFN with DISPATCHVAL.
   Just a helper utility for point-free multi-method
   implementation registration."
  [multifn dispatchval impl]
  `(defmethod ~multifn ~dispatchval [& xs#] (apply ~impl xs#)))

(defmethod part1
  :default
  [day]
  (throw (Exception.
           (format "Failed to run, no part1 implementation for day %s!" day))))

(defmethod part2
  :default
  [day]
  (throw (Exception.
           (format "Failed to run, no part2 implementation for day %s!" day))))

(defn -main
  "The entrypoint of my advent-of-code 2020 Clojure code.
   Call it w/o args to show all results.
   Call it w/ 'xy' to show day 'xy' result."
  ([]
   (-main nil))
  ([day]
   (->> (io/file "./")
        file-seq
        (map #(re-find #"day\_(\d+)$" (.getName %)))
        (filter some?)
        (map last)
        ((fn [x] (if (nil? day)
                  x
                  (filter #(= % day) x))))
        sort
        (map #(do
                (require (symbol (format "day_%s.solution" %)))
                (println "day" %)
                (println "\tpart 1:" (part1 %))
                (println "\tpart 2:" (part2 %))
                ))
        doall)))
