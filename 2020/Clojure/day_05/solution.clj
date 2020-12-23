(ns day_05.solution
  (:require [clojure.string :as str]
            [clojure.set :as sset]
            [main :as main :refer [defoverload]]))

(def day "05")

(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (->> file
       slurp
       str/split-lines
       (map identity)))

(defn binary-search-row-and-col
  "Implement a modified binary search based on problem desc."
  [low high indicators is-row?]
  (loop [low low
         high high
         indicators indicators]
    (if-let [indicator (first indicators)]
      (let [mid (quot (+ low high) 2)]
        (case indicator
          ;; note the difference between char and string in clojure!
          \F (recur low mid (rest indicators))
          \B (recur (inc mid) high (rest indicators))
          \L (recur low mid (rest indicators))
          \R (recur (inc mid) high (rest indicators))))
      (if is-row?
        ;; keeps the lower of the two for row-searching
        low
        ;; keeps the upper of the two for row-searching
        high))))

(defn part1
  [_]
  (letfn [(locate&compute [s]
            (let [row-indicators (take 7 s)
                  col-indicators (drop 7 s)]
              (+ (* 8 (binary-search-row-and-col 0 127 row-indicators true))
                 (binary-search-row-and-col 0 7 col-indicators false))))]
   (let [inputs (get-lines "day_05/inputs.txt")]
    (->> inputs
         (map locate&compute)
         (apply max)))))

(defn part2
  [_]
  (letfn [(locate [s]
            (let [row-indicators (take 7 s)
                  col-indicators (drop 7 s)]
              [(binary-search-row-and-col 0 127 row-indicators true)
               (binary-search-row-and-col 0 7 col-indicators false)]))
          (compute [[row col]] (+ (* 8 row) col))
          (valid? [s [x y]]
            (let [computed (compute [x y])]
              (when (and (s (dec computed))
                         (s (inc computed)))
                true)))]
    (let [pairs (->> (get-lines "day_05/inputs.txt") (map locate))
          scores (set (map compute pairs))
          coords (reduce conj #{} pairs)
          array (make-array Integer/TYPE 128 8)
          网格 (set (for [x (range 128)
                        y (range 8)]
                    [x y]))]
      (->> (sset/difference 网格 coords)
           (filter #(valid? scores %))
           first
           compute))))

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
